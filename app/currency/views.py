from currency.models import ContactUs
from currency.utils import foo

from django.http import HttpResponse
from django.shortcuts import render # noqa

# Create your views here.


def hello_world(requsts):
    return HttpResponse('Hello World')


def some_foo(requsts):
    tests = foo()
    return HttpResponse(tests)


def contact_us(requsts):
    resalt = []
    contacts = ContactUs.objects.all()
    for contact in contacts:
        resalt.append(
            f'email: {contact.email_from} subject: {contact.subject} message: {contact.message} </br>'
        )
    return HttpResponse(resalt)

