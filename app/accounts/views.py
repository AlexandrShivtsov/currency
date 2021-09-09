from accounts.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    fields = (
        'first_name',
        'last_name',
    )
    success_url = reverse_lazy('index')
    template_name = 'my-profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class SuccessPasswordResetView(TemplateView):
    template_name = 'index.html'
