import uuid

from accounts.models import User
from accounts.tasks import activate

from django import forms
from django.conf import settings
from django.urls import reverse


class SingUpForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField()

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password1'] != cleaned_data['password2']:
            raise forms.ValidationError('Passwords do not match!')
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        instance.is_active = False
        instance.username = str(uuid.uuid4())
        instance.set_password(self.cleaned_data['password1'])
        activation_path = reverse("accounts:activate-user", args=[instance.username])
        activate(f'{settings.HTTP_SCHEMA}://{settings.DOMAIN}{activation_path}',
                 instance.email,)

        if commit:
            instance.save()

        return instance
