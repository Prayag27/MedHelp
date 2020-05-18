from django.shortcuts import render
from .forms import GetDoctorDetails, GetHospitalDetails
# Create your views here.
def Register_Doctor(request):
    if request.method == "POST":
        form = GetDoctorDetails(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = GetDoctorDetails()
    return render(request, 'DoctorDetails.html', {'form': form})

def Register_Hospital(request):
    if request.method == "POST":
        form = GetHospitalDetails(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = GetHospitalDetails()
    return render(request, 'HospitalDetails.html', {'form': form})