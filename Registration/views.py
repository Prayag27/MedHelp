from django.shortcuts import render
from .forms import GetDoctorDetails, GetHospitalDetails
from Database import ManageDB


def Register_Doctor(request):
    if request.method == "POST":
        form = GetDoctorDetails(request.POST)
        if form.is_valid():
            print('VALID')
            post = form.save(commit=False)
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
                'patients': post.patientId,
            }
            print(doc)
            ManageDB.addDoctor(doc)
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