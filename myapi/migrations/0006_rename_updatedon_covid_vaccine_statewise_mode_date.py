# Generated by Django 3.2.6 on 2021-08-11 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_rename_state_unionterritory_covid_india_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='covid_vaccine_statewise_mode',
            old_name='UpdatedOn',
            new_name='Date',
        ),
    ]
