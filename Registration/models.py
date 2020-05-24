from django.db import models
from django.db.models import CharField, Model
from multiselectfield import MultiSelectField
from .Lists import ResourceList, IllnessList
from django.conf import settings
from django.db import models
from django.utils import timezone


class patient(models.Model):
	name = models.CharField(max_length=50)
	lat = models.IntegerField()
	long = models.IntegerField()
	illnesses = MultiSelectField(choices=IllnessList, max_choices=len(IllnessList), default=None)
	currentPrescriptions = models.CharField(max_length=500)
	isAdmitted = models.BooleanField(default=None)
	hId = models.ForeignKey('HospitalDetails', on_delete= models.CASCADE, default=None, blank= True, null=True)
	pId = models.IntegerField(primary_key=True)


class HospitalDetails(models.Model):
	hospitalId = models.IntegerField(primary_key=True)
	doctorIds = models.CharField(max_length=200, blank=True)
	#Resources = MultiSelectField(choices=ResourceList, max_choices=len(ResourceList), default='R1')
	ResourceQuantity = models.CharField(max_length=200)
	lat = models.IntegerField(default=0)
	long = models.IntegerField(default=0)
	patientIds = models.CharField(max_length=100, default=None, null=True)


class DoctorDetails(models.Model):
	dId = models.IntegerField(primary_key=True, default=None)
	name = models.CharField(max_length=50)
	visStart = models.TimeField(default=timezone.now)
	visEnd = models.TimeField(default=timezone.now)
	lat = models.IntegerField(default=0)
	long = models.IntegerField(default=0)
	hospShiftStart = models.TimeField(default=timezone.now)
	hospShiftEnd = models.TimeField(default=timezone.now)
	hId = models.ForeignKey(HospitalDetails, on_delete= models.CASCADE, default=None, blank= True, null=True)
	patientId =  models.CharField(max_length=100)

"""
class ResourceDetails(models.Model):
	total_beds = models.IntegerField(default=0)
	total_nonMed_staff = models.IntegerField(default=0)
"""

class IdNo(models.Model):
	IdNum = models.IntegerField(default=None)
	name = models.CharField(max_length=90)