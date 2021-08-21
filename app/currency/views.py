from currency.forms import SourceForm
from currency.models import ContactCreate, ContactUs, Rate, Source

from django.conf import settings # noqa
from django.core.mail import send_mail # noqa
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


class ContactusCreateView(CreateView):
    queryset = ContactCreate.objects.all()
    success_url = reverse_lazy('index')
    template_name = 'contactus-create.html'
    fields = (
        'email_to',
        'subject',
        'message',
    )

    def form_valid(self, form):
        email_to = form.cleaned_data['email_to']
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        full_email_massage = f'''
        Email From: {email_to}
        Message: {message}
        '''
        from currency.tasks import contact
        contact.apply_async(args=(subject, full_email_massage))
        # send_mail(
        #     subject,
        #     full_email_massage,
        #     settings.EMAIL_HOST_USER,
        #     [settings.SUPPORT_EMAIL],
        #     fail_silently=False,
        # )
        return super().form_valid(form)


class CurrencyRateListView(ListView):
    context_object_name = 'source_list'
    queryset = Rate.objects.all()
    template_name = 'currency_rate_list.html'
