from django.db import models


# Create your models here.
class userBooking(models.Model):
    name = models.CharField(max_length=20, null=True, blank=False)
    age = models.IntegerField(default=18, null=True, blank=False)
    sex = models.CharField(max_length=10, blank=False, null=True)
    email_id = models.EmailField(max_length=30, null=True, blank=False)
    date = models.DateField(null=True, blank=False)
    mobileNum = models.IntegerField(null=False, blank=False, primary_key=True)
    center_name = models.CharField(max_length=50, null=True, blank=False)


class VaccinationCenters(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    centre_name = models.CharField(max_length=50)
    center_address = models.CharField(max_length=100)
    empty_slots = models.IntegerField(default=10)
    date = models.DateField(null = True, blank = False)


class AdminData(models.Model):
    user_name = models.CharField(max_length=20, null=True, blank=False)
    password = models.CharField(max_length=20, null=True, blank=False)
