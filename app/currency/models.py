from currency import model_choces as mch

from django.db import models


# Create your models here.


class ContactUs(models.Model):
    email_from = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2056)


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)

    avatar = models.FileField(
        blank=True,
        null=True,
        default=None,
        upload_to='avatars',
    )


class ContactCreate(models.Model):
    email_to = models.EmailField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2056)
    created = models.DateTimeField(auto_now_add=True)


class SourceBank(models.Model):
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=64, unique=True, editable=False)


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    # source = models.CharField(max_length=32)
    source = models.ForeignKey(
        SourceBank,
        related_name='rates',
        on_delete=models.CASCADE,)
    currency_type = models.CharField(max_length=3,
                                     choices=mch.RATE_TAPES,
                                     blank=False,
                                     null=False,
                                     default=mch.TAPE_USD)


class ResponseLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    status_code = models.PositiveSmallIntegerField()
    path = models.CharField(max_length=255)
    response_time = models.PositiveSmallIntegerField(
        help_text='im milliseconds'
    )
    request_method = models.CharField(max_length=10, choices=mch.RATE_METHODS)
