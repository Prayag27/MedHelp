from django import forms
from .models import DoctorDetails , HospitalDetails, patient, IdNo


class GetDoctorDetails(forms.ModelForm):

    class Meta:
        model = DoctorDetails
        fields = ('dId','name','visStart', 'visEnd', 'hospShiftStart', 'hospShiftEnd', 'patientId')


class GetHospitalDetails(forms.ModelForm):

    class Meta:
        model = HospitalDetails
        fields = ('hospitalId' , 'ResourceQuantity','doctorIds', 'patientIds')


class GetPatientDetails(forms.ModelForm):
    class Meta:
        model = patient
        fields = ('name', 'illnesses', 'currentPrescriptions', 'isAdmitted', 'hId', 'pId')


class GetId(forms.ModelForm):
    class Meta:
        model = IdNo
        fields = ('IdNum', 'name')