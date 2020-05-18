from django import forms

from .models import DoctorDetails , HospitalDetails

class GetDoctorDetails(forms.ModelForm):

    class Meta:
        model = DoctorDetails
        fields = ('DocId','hospitalId','Name','VisitingHoursFrom', 'VisitingHoursTo')

class GetHospitalDetails(forms.ModelForm):

    class Meta:
        model = HospitalDetails
        fields = ('HospitalName', 'hospitalId','Resources','vacancy')