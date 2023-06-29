# Generated by Django 4.2.2 on 2023-06-28 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covidVaccineCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('email_id', models.EmailField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('mobileNum', models.IntegerField(max_length=10)),
            ],
        ),
    ]
