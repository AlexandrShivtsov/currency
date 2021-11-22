from celery import shared_task

from django.conf import settings
from django.core.mail import send_mail


@shared_task
def activate(activate_link, email_to):
    subject = 'Activate tour account today!',
    full_email_massage = f'''
           Hello!

           Here is your activation link {activate_link}
           '''

    send_mail(
        subject,
        full_email_massage,
        settings.EMAIL_HOST_USER,
        [email_to],
        fail_silently=False,
    )
