from accounts.forms import SingUpForm
from accounts.models import User

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, RedirectView, TemplateView, UpdateView


class MyProfileView(LoginRequiredMixin, UpdateView):
    queryset = User.objects.all()
    fields = (
        'first_name',
        'last_name',
        'avatar',
    )
    success_url = reverse_lazy('index')
    template_name = 'my-profile.html'

    def get_object(self, queryset=None):
        return self.request.user


class SuccessPasswordResetView(TemplateView):
    template_name = 'index.html'


class SingUpView(CreateView):
    model = User
    template_name = 'sing-up.html'
    success_url = reverse_lazy('index')
    form_class = SingUpForm


class ActivateUserView(RedirectView):
    pattern_name = 'index'

    def get_redirect_url(self, *args, **kwargs):
        username = kwargs.pop('username')
        user = get_object_or_404(User, username=username, is_active=False)
        user.is_active = True
        user.save(update_fields=('is_active', ))
        return super().get_redirect_url(*args, **kwargs)
