from currency.forms import SourceForm
from currency.models import ContactUs, Source

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

# Create your views here.


def hello_world(request):
    return HttpResponse('Hello World')


def contact_us(request):
    contacts = ContactUs.objects.all()
    context = {
        'rate_list': contacts
    }
    return render(request, 'rate_list.html', context=context)


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


def source_list(request):
    source_list = Source.objects.all()
    context = {
        'source_list': source_list
    }
    return render(request, 'source-list.html', context=context)


def create_source(request):
    if request.method == 'POST':
        form = SourceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source-list/')
    elif request.method == 'GET':
        form = SourceForm()
    context = {
        'form': form,
    }
    return render(request, 'create-source.html', context=context)


def details_source(request, source_id):
    source = get_object_or_404(Source, id=source_id)
    context = {
        'source': source
    }
    return render(request, 'details-source.html', context=context)


def update_source(request, source_id):
    source = get_object_or_404(Source, id=source_id)
    if request.method == 'POST':
        form = SourceForm(request.POST, instance=source)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/source-list/')
    elif request.method == 'GET':
        form = SourceForm(instance=source)
    context = {
        'form': form,
    }
    return render(request, 'update-source.html', context=context)


def delete_source(request, source_id):
    source = get_object_or_404(Source, id=source_id)
    if request.method == 'POST':
        source.delete()
        return HttpResponseRedirect('/source-list/')
    context = {
        'source': source,
    }
    return render(request, 'delete-source.html', context=context)
