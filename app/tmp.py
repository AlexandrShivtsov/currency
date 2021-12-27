from django.core.mail import send_mail
# from currency.models import Rate
# import random

send_mail(
    'Subject here',
    'Here is the message.',
    'ShivtsovaTestMail@gmail.com',
    ['ShivtsovaTestMail@gmail.com'],
    fail_silently=False,
)
