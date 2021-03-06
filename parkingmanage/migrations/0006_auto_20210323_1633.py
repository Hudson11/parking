# Generated by Django 3.1.7 on 2021-03-23 19:33

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('parkingmanage', '0005_auto_20210322_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='reservation',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='parking',
            name='minutes',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='parking',
            name='plate',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='invalid_plate', message='This format is not valid, try using the standard AAA-9999', regex=re.compile('^[a-zA-Z]{3}-[0-9]{4}$'))]),
        ),
    ]
