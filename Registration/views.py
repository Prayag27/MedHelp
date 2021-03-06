from typing import Dict, Any

from django.shortcuts import render
from .forms import GetDoctorDetails, GetHospitalDetails,GetPatientDetails, GetId
from Database import ManageDB
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/Profile')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'Profile.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/Profile')
        else:
            form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})


def Register_Doctor(request):
    if request.method == "POST":
        form = GetDoctorDetails(request.POST)
        if form.is_valid():
            print('VALID')
            post = form.save(commit=False)
            print(post.patientId.split)
            doc = {
                'dId': post.dId,
                'name': post.name,
                'visStart': int(str(post.visStart.hour) + str(post.visStart.minute)),
                'visEnd': int(str(post.visEnd.hour) + str(post.visEnd.minute)),
                'lat': post.lat,
                'long': post.long,
                'hospShiftStart': int(str(post.hospShiftStart.hour) + str(post.hospShiftStart.minute)),
                'hospShiftEnd': int(str(post.hospShiftEnd.hour) + str(post.hospShiftEnd.minute)),
                'hId': post.hId,
                'patients': [int(i) for i in post.patientId.split()],
            }
            print(doc)
            ManageDB.addDoctor(doc)
            post.save()
            return render(request, 'Dashboard.html')
    else:
        form = GetDoctorDetails()
    return render(request, 'DoctorDetails.html', {'form': form})

def homeHospital(request):
    return render(request,'homepage.html')

def Register_Hospital(request):
    if request.method == "POST":
        form = GetHospitalDetails(request.POST)
        if form.is_valid():
            print('VALID')
            post = form.save(commit=False)
            hosp = {
                'doctors': post.dId.dId,
                'resourceToQuantity': post.ResourceToQuant,
                'hId': post.hospitalId,
                'lat': post.lat,
                'long': post.long,
                'patients': post.pId.split()
            }
            print(hosp)
            ManageDB.addHospital(hosp)
            post.save()
            return render(request, 'DataAccess.html')
    else:
        form = GetHospitalDetails()
    return render(request, 'HospitalDetails.html', {'form': form})

def Register_patient(request):
    if request.method == "POST":
        form = GetPatientDetails(request.POST)
        if form.is_valid():
            print('VALID')
            post = form.save(commit=False)
            pat = {
                'name': post.name,
                'lat': post.lat,
                'long': post.long,
                'illnesses':post.illnesses,
                'currentPrescriptions':post.currentPrescriptions,
                'isAdmitted':post.isAdmitted,
                'hId': post.hId.hospitalId,
                'pId': post.pId,
            }
            print(pat)
            ManageDB.addPatient(pat)
            post.save()
            return render(request, 'Dashboard.html')
    else:
        form = GetPatientDetails()
    return render(request, 'PatientDetails.html', {'form': form})

def Profile(request):
    return render(request, 'Profile.html')

def FetchData(request):
    if request.method == 'POST':
        form = GetId(request.POST)
        if form.is_valid():
            print('VALID')
            post = form.save(commit=False)
            print(post.IdNum)
            data = ManageDB.docGetPatients(post.IdNum)
            print(data)
            context = {
                'data': data
            }
            post.save()
            return render(request, 'ViewData.html', context)
    else:
        form = GetId()
    return render(request, 'DataAccess.html', {'form': form})

def ViewData(request, data):

    return render(request, 'ViewData.html', data)