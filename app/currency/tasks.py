from decimal import Decimal

from bs4 import BeautifulSoup

from celery import shared_task

from currency import consts
from currency import model_choces as mch

from django.core.mail import send_mail

import requests

from settings import settings


def round_currency(nam):
    return Decimal(nam).quantize(Decimal('.01'))


@shared_task
def debug_task(sleep_time: int = 2):
    pass


@shared_task
def contact(subject, full_email_massage):
    send_mail(
        subject,
        full_email_massage,
        settings.EMAIL_HOST_USER,
        [settings.SUPPORT_EMAIL],
        fail_silently=False,
    )


@shared_task
def parse_privatbank():
    from currency.models import Rate, SourceBank
    privatbank_api_url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    response = requests.get(privatbank_api_url)

    response.raise_for_status()

    rates = response.json()

    source = SourceBank.objects.get_or_create(
        code_name=consts.CODE_NAME_PRIVATBANK,
        defaults={'name': 'PrivatBank'},
    )[0]
    available_currency_types = {
        'USD': mch.TAPE_USD,
        'EUR': mch.TAPE_EUR,
    }

    for rate in rates:
        currency_type = rate['ccy']
        if currency_type in available_currency_types:
            buy = round_currency(rate['buy'])
            sale = round_currency(rate['sale'])
            last_rate = Rate.objects.filter(
                currency_type=currency_type,
                source=source
            ).order_by('created').last()

            if (
                last_rate is None or
                last_rate.sale != sale or
                last_rate.buy != buy
            ):

                Rate.objects.create(
                    sale=sale,
                    buy=buy,
                    currency_type=currency_type,
                    source=source
                )


@shared_task
def parse_monobank():
    from currency.models import Rate, SourceBank
    monobank_api_url = 'https://api.monobank.ua/bank/currency'
    response = requests.get(monobank_api_url)

    response.raise_for_status()

    rates = response.json()

    source = SourceBank.objects.get_or_create(
        code_name=consts.CODE_NAME_MONOBANK,
        defaults={'name': 'MonoBank'},
    )[0]
    available_currency_types = {840: 'USD', 978: 'EUR'}

    for rate in rates:
        if rate['currencyCodeA'] in available_currency_types and rate['currencyCodeB'] == 980:
            currency_type = available_currency_types[rate['currencyCodeA']]
            buy = round_currency(rate['rateBuy'])
            sale = round_currency(rate['rateSell'])

            last_rate = Rate.objects.filter(
                currency_type=currency_type,
                source=source
            ).order_by('created').last()

            if (
                last_rate is None or
                last_rate.sale != Decimal(sale) or
                last_rate.buy != Decimal(buy)
            ):

                Rate.objects.create(
                    sale=sale,
                    buy=buy,
                    currency_type=currency_type,
                    source=source
                )


@shared_task
def parse_vkurse():
    from currency.models import Rate
    vkurse_api_url = 'http://vkurse.dp.ua/course.json'
    response = requests.get(vkurse_api_url)

    response.raise_for_status()

    rates = response.json()
    source = 'vkurse'
    available_currency_types = {'Dollar': 'USD', 'Euro': 'EUR'}

    for rate in rates:
        if rate in available_currency_types:
            currency_type = available_currency_types[rate]
            buy = round_currency(rates[rate]['buy'])
            sale = round_currency(rates[rate]['sale'])

            last_rate = Rate.objects.filter(
                currency_type=currency_type,
                source=source
            ).order_by('created').last()

            if (
                last_rate is None or
                last_rate.sale != Decimal(sale) or
                last_rate.buy != Decimal(buy)
            ):

                Rate.objects.create(
                    sale=sale,
                    buy=buy,
                    currency_type=currency_type,
                    source=source
                )


@shared_task
def parse_minfin():
    from currency.models import Rate
    alfabank_url = 'https://minfin.com.ua/currency/banks/'
    response = requests.get(alfabank_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'lxml')

    source = 'minfin'
    start_point = soup.find('td', class_="mfm-text-nowrap")
    currency_type_usd = 'USD'
    usd_buy = round_currency(start_point.contents[0])
    usd_sale = round_currency(start_point.contents[-1])

    last_rate = Rate.objects.filter(
        currency_type=currency_type_usd,
        source=source
    ).order_by('created').last()

    if (
        last_rate is None or
        last_rate.sale != Decimal(usd_sale) or
        last_rate.buy != Decimal(usd_buy)
    ):

        Rate.objects.create(
            sale=usd_sale,
            buy=usd_buy,
            currency_type=currency_type_usd,
            source=source
        )

    currency_type_eur = 'EUR'
    euro = start_point.find_next('td', class_="mfcur-table-cur")
    eur_buy = euro.find_next('td', class_="mfm-text-nowrap").contents[0]
    eur_sale = euro.find_next('td', class_="mfm-text-nowrap").contents[-1]

    last_rate = Rate.objects.filter(
        currency_type=currency_type_eur,
        source=source
    ).order_by('created').last()

    if (last_rate is None or
            last_rate.sale != Decimal(eur_sale) or
            last_rate.buy != Decimal(eur_buy)):
        Rate.objects.create(
            sale=eur_sale,
            buy=eur_buy,
            currency_type=currency_type_eur,
            source=source
        )


@shared_task
def pars_finance():
    from currency.models import Rate
    finance_url = 'https://finance.i.ua/'
    response = requests.get(finance_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'lxml')

    source = 'finance'
    currency_type_usd = 'USD'

    start_point_usd = soup.find('span', class_="value -increase")
    usd_buy = round_currency(soup.find('span', class_="value -increase").contents[0].text)
    usd_sale = round_currency(start_point_usd.find_next('span', class_="value -increase").contents[0].text)

    last_rate = Rate.objects.filter(
        currency_type=currency_type_usd,
        source=source
    ).order_by('created').last()

    if (
        last_rate is None or
        last_rate.sale != Decimal(usd_sale) or
        last_rate.buy != Decimal(usd_buy)
    ):

        Rate.objects.create(
            sale=usd_sale,
            buy=usd_buy,
            currency_type=currency_type_usd,
            source=source
        )

    currency_type_eur = 'EUR'
    start_point_eur = start_point_usd.find_next('span', class_="value -increase")

    eur_buy = start_point_eur.find_next('span', class_="value -decrease").contents[0].text

    euro_sale_point = start_point_eur.find_next('span', class_="value -decrease")
    eur_sale = euro_sale_point.find_next('span', class_="value -increase").contents[0].text

    last_rate = Rate.objects.filter(
        currency_type=currency_type_eur,
        source=source
    ).order_by('created').last()

    if (
        last_rate is None or
        last_rate.sale != Decimal(eur_sale) or
        last_rate.buy != Decimal(eur_buy)
    ):

        Rate.objects.create(
            sale=eur_sale,
            buy=eur_buy,
            currency_type=currency_type_eur,
            source=source
        )
