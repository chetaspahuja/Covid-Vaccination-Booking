# Generated by Django 4.2.2 on 2023-06-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_rename_covidvaccinecenter_userbooking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbooking',
            name='time',
        ),
        migrations.AlterField(
            model_name='userbooking',
            name='date',
            field=models.DateField(),
        ),
    ]
