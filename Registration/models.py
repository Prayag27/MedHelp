from django.db import models
from multiselectfield import  MultiSelectField
# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone

class HospitalDetails(models.Model):
	hospitalId= models.UUIDField(primary_key=True)
	"""ResourceList = (
		('R1','Ambulatory surgical center'),
		('R2','Birth center'), 
		('R3','Dialysis Center'),
		('R4','Imaging and radiology center'),
		('R5,''Mental health and addiction treatment center'),
		('R6','Orthopedic center'),
	)"""
	ResourceList = (
        ('R1', 'Ambulatory surgical center'),
        ('R2', 'Birth center'),
        ('R3', 'Dialysis Center'),
    )
	Resources = MultiSelectField(choices=ResourceList, max_choices= len(ResourceList), default='R1')
	#shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default='M')
	vacancy = models.BigIntegerField(default=0)
	HospitalName = models.TextField(default=None)

class DoctorDetails(models.Model):
	DocId = models.UUIDField(primary_key=True)
	hospitalId = models.ForeignKey(HospitalDetails, on_delete=models.CASCADE)
	#patientId = models.ForeignKey()
	Name = models.TextField()
	VisitingHoursFrom = models.TimeField(default=timezone.now)
	VisitingHoursTo = models.TimeField(default=timezone.now)
	"""discharge_date = models.DateTimeField(blank=True, null=True)
	attending_doctor_name= models.CharField(max_length=200)
	allocated_bed=models.IntegerField()
	f1 = models.TextField()
	
	def AllocateBed(self):
		self.free_beds-=1
"""
class ResourceDetails(models.Model):
	total_beds=models.IntegerField(default=0)
	total_nonMed_staff=models.IntegerField(default=0)