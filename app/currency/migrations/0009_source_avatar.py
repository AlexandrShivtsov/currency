# Generated by Django 3.2.5 on 2021-11-18 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0008_auto_20210827_1921'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='avatar',
            field=models.FileField(blank=True, default=None, null=True, upload_to='avatars'),
        ),
    ]