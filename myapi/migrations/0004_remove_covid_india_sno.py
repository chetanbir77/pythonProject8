# Generated by Django 3.2.6 on 2021-08-10 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_covid_india_statewise_testing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='covid_india',
            name='Sno',
        ),
    ]
