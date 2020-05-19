'''This is the script fot initialising the database
It should not be touched once the database has been 
created. It is used to set up the initial structure 
of the database which shall support the queries 
written in Manage.py'''

from firebase import firebase
import pickle

print('Setting up database')
DBPATH='https://hospitalapp-b7f04.firebaseio.com/'
db=firebase.FirebaseApplication('https://hospitalapp-b7f04.firebaseio.com/')

print('Setting up Hospital collection')
hospNull=db.post('/Hospital','hospnull')
print('Setting up Patient collection')
patNull=db.post('/Patient','patnull')
print('Setting up Doctor collection')
docNull=db.post('/Doctor','docnull')
print('Setting up Prescription collection')
prescNull=db.post('/Prescription','prescnull')


print('Initialising DoctorID.bin')
fstr=open('Binaries/DoctorID.bin',"wb")
pickle.dump({'docnull':docNull['name']},fstr)
fstr.close()

print('Initialising HsopitalID.bin')
fstr=open('Binaries/HospitalID.bin',"wb")
pickle.dump({'hospnull':hospNull['name']},fstr)
fstr.close()

print('Initialising PatientID.bin')
fstr=open('Binaries/PatientID.bin',"wb")
pickle.dump({'patnull':patNull['name']},fstr)
fstr.close()

print('Initialising PrescriptionID.bin')
fstr=open('Binaries/PrescriptionID.bin',"wb")
pickle.dump({'prescnull':prescNull['name']},fstr)
fstr.close()
print('Done ')
