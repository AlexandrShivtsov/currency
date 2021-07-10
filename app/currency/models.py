from django.db import models

# Create your models here.

class ContactUs(models.Model):
    email_from = models.EmailField(max_length=50)
    subject = models.CharField(max_length=64)
    message = models.CharField(max_length=200 )