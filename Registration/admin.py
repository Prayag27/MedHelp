# Register your models here.
from django.contrib import admin
from .models import DoctorDetails, HospitalDetails, patient

admin.site.register(DoctorDetails)
admin.site.register(HospitalDetails)
admin.site.register(patient)