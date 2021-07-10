from django.shortcuts import render
from django.http import HttpResponse
from currency.utils import foo

# Create your views here.

def hello_world(requsta):
    return HttpResponse('Hello World')

def some_foo(requsts):
    tests = foo()
    return HttpResponse(tests)