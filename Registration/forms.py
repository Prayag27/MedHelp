from django import forms
from .models import DoctorDetails , HospitalDetails


class GetDoctorDetails(forms.ModelForm):

    class Meta:
        model = DoctorDetails
        fields = ('dId','name','visStart', 'visEnd', 'lat', 'long', 'hospShiftStart', 'hospShiftEnd', 'hId', 'patientId')


class GetHospitalDetails(forms.ModelForm):

    class Meta:
        model = HospitalDetails
        fields = ('dId', 'ResourceToQuant','hospitalId','lat','long', 'pId')