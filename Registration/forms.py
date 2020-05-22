from django import forms
from .models import DoctorDetails , HospitalDetails, patient


class GetDoctorDetails(forms.ModelForm):

    class Meta:
        model = DoctorDetails
        fields = ('dId','name','visStart', 'visEnd', 'lat', 'long', 'hospShiftStart', 'hospShiftEnd', 'hId', 'patientId')


class GetHospitalDetails(forms.ModelForm):

    class Meta:
        model = HospitalDetails
        fields = ('dId', 'ResourceToQuant','hospitalId','lat','long', 'pId')


class GetPatientDetails(forms.ModelForm):
    class Meta:
        model = patient
        fields = ('name', 'lat', 'long', 'illnesses', 'currentPrescriptions', 'isAdmitted', 'hId', 'pId')
