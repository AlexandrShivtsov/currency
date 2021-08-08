# Generated by Django 3.2.5 on 2021-08-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0002_source'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactCreate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.CharField(max_length=2056)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=2056),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=255),
        ),
    ]