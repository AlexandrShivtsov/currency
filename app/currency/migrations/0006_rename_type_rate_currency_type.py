# Generated by Django 3.2.5 on 2021-08-21 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0005_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='type',
            new_name='currency_type',
        ),
    ]