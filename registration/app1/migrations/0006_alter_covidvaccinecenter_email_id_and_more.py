# Generated by Django 4.2.2 on 2023-06-28 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_covidvaccinecenter_email_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidvaccinecenter',
            name='email_id',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='covidvaccinecenter',
            name='mobileNum',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='covidvaccinecenter',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='covidvaccinecenter',
            name='sex',
            field=models.CharField(max_length=10),
        ),
    ]