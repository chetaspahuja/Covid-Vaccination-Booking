from django.contrib import admin
from .models import userBooking,VaccinationCenters, AdminData

# Register your models here.

@admin.register(userBooking)
@admin.register(AdminData)
@admin.register(VaccinationCenters)

class DataAdmin(admin.ModelAdmin):
    pass 
