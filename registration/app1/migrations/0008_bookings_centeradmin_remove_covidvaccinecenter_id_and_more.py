# Generated by Django 4.2.2 on 2023-06-28 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_alter_covidvaccinecenter_email_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='bookings',
            fields=[
                ('patient', models.CharField(max_length=20)),
                ('centre_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('slot_date', models.DateField()),
                ('slot_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='centerAdmin',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('centre_name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='covidvaccinecenter',
            name='id',
        ),
        migrations.AlterField(
            model_name='covidvaccinecenter',
            name='mobileNum',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='covidvaccinecenter',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
