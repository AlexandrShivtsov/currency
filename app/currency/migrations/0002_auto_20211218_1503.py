# Generated by Django 3.2.5 on 2021-12-18 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='email_from',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='currency.sourcebank'),
        ),
    ]
