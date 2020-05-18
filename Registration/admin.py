# Register your models here.
from django.contrib import admin
from .models import DoctorDetails, HospitalDetails

admin.site.register(DoctorDetails)
admin.site.register(HospitalDetails)