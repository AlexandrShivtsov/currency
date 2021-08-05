from currency.forms import SourceForm
from currency.models import ContactUs, Source


from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView
# Create your views here.


def contact_us(request):
    contacts = ContactUs.objects.all()
    context = {
        'rate_list': contacts
    }
    return render(request, 'rate_list.html', context=context)


class SourceLoginView(TemplateView):
    template_name = 'login.html'


class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source-list.html'


class SourceCreateView(CreateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'create-source.html'


class SourceDetailsView(DetailView):
    queryset = Source.objects.all()
    template_name = 'details-source.html'


class SourceUpdateView(UpdateView):
    queryset = Source.objects.all()
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'update-source.html'


class SourceDeleteView(DeleteView):
    queryset = Source.objects.all()
    success_url = reverse_lazy('currency:source-list')
    template_name = 'delete-source.html'
