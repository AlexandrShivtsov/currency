from django.db import models

# Create your models here.


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2056)


class Source(models.Model):
    source_url = models.URLField(max_length=255)
    name = models.CharField(max_length=64)


class ContactCreate(models.Model):
    email_to = models.EmailField(max_length=50)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=2056)
    created = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=32)
    currency_type = models.CharField(max_length=3)
