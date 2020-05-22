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
	currentPrescriptions = models.TextField()
	isAdmitted = models.BooleanField(default=None)
	hId = models.ForeignKey('HospitalDetails', related_name='+', on_delete= models.CASCADE, default=None, blank= True, null=True)
	pId = models.IntegerField(primary_key=True)


class HospitalDetails(models.Model):
	dId = models.ForeignKey('DoctorDetails', related_name='+',max_length= 4 ,on_delete= models.CASCADE, default=None, blank= True, null=True)
	#Resources = MultiSelectField(choices=ResourceList, max_choices=len(ResourceList), default='R1')
	ResourceToQuant = models.TextField()
	hospitalId = models.IntegerField(primary_key=True)
	lat = models.IntegerField(default=0)
	long = models.IntegerField(default=0)
	pId = models.ForeignKey('Patient', related_name='+', on_delete= models.CASCADE, default=None, blank= True, null=True)


class DoctorDetails(models.Model):
	dId = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=50)
	visStart = models.TimeField(default=timezone.now)
	visEnd = models.TimeField(default=timezone.now)
	lat = models.IntegerField(default=0)
	long = models.IntegerField(default=0)
	hospShiftStart = models.TimeField(default=timezone.now)
	hospShiftEnd = models.TimeField(default=timezone.now)
	hId = models.ForeignKey('HospitalDetails', related_name='+', on_delete= models.CASCADE, default=None, blank= True, null=True)
	patientId = models.ForeignKey('Patient', related_name= '+', on_delete=models.CASCADE, default=None, blank= True, null=True)

"""
class ResourceDetails(models.Model):
	total_beds = models.IntegerField(default=0)
	total_nonMed_staff = models.IntegerField(default=0)
"""