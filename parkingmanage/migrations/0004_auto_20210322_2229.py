# Generated by Django 3.1.7 on 2021-03-22 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkingmanage', '0003_auto_20210322_2220'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parking',
            options={'ordering': ['id'], 'verbose_name': 'Parking', 'verbose_name_plural': 'Parking`s'},
        ),
        migrations.AlterField(
            model_name='parking',
            name='minutes',
            field=models.CharField(default='', editable=False, max_length=20),
        ),
    ]
