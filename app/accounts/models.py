import django.contrib.auth.validators
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    username = models.CharField(error_messages={'unique': 'A user with that username already exists.'},
                                help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                max_length=150,
                                unique=True,
                                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                                verbose_name='username')

    phone = models.CharField(
        blank=True,
        max_length=11,
        null=True,
        default=None,
    )

    email = models.EmailField('email address', blank=True, unique=True)
