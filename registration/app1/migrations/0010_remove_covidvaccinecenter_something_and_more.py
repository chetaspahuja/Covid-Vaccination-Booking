# Generated by Django 4.2.2 on 2023-06-28 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_covidvaccinecenter_something'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='covidvaccinecenter',
            name='something',
        ),
        migrations.AlterField(
            model_name='covidvaccinecenter',
            name='age',
            field=models.IntegerField(default=18, null=True),
        ),
        migrations.AlterField(
            model_name='covidvaccinecenter',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]