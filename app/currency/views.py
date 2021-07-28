from currency.models import ContactUs
from currency.utils import foo

from django.http import HttpResponse
from django.shortcuts import render # noqa

# Create your views here.


def hello_world(requst):
    return HttpResponse('Hello World')


def some_foo(requst):
    tests = foo()
    return HttpResponse(tests)


def contact_us(requst):
    contacts = ContactUs.objects.all()
    context = {
        'rate_list': contacts
    }
    return render(requst, 'rate_list.html', context=context)


def index(requst):
    return render(requst, 'index.html')


def login(requst):
    return render(requst, 'login.html')
