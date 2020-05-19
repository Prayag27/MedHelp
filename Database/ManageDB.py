import pickle
from firebase import firebase

db=firebase.FirebaseApplication('https://hospitalapp-b7f04.firebaseio.com/')

patDict=pickle.load(open('Database/Binaries/PatientID.bin','rb'))
prescDict=pickle.load(open('Database/Binaries/PrescriptionID.bin','rb'))
hospDict=pickle.load(open('Database/Binaries/HospitalID.bin','rb'))
docDict=pickle.load(open('Database/Binaries/DoctorID.bin','rb'))

patDictAltered=False
prescDictAltered=False
hospDictAltered=False
docDictAltered=False


def closeModule():
    '''Dont forget to call this function at the end of usage
        otherwise database consistency will be seriously 
        affected. Sudden termination through external signals
        and interrupts will result in inconsistencies. Therefore,
        always call this function before exit
    '''

    if patDictAltered:
        pickle.dump(patDict,open('Database/Binaries/PatientID.bin','wb'))
    if prescDictAltered:
        pickle.dump(prescDict,open('Database/Binaries/PrescriptionID.bin','wb'))
    if hospDictAltered:
        pickle.dump(hospDict,open('Database/Binaries/HospitalID.bin','wb'))
    if docDictAltered:
        pickle.dump(patDict,open('Database/Binaries/DoctorID.bin','wb'))

def addDoctor(docDetailsDict):
    '''All details of the doctor to be added must be supplied in the 
    form of a dcitionary stored in docDeatilsDict.
    '''

    d=docDetailsDict

    if('dId' not in d or 'name' not in d or 'visStart' not in d or 
        'visEnd' not in d or 'lat' not in d or 'long' not in d or 
        'hospShiftStart' not in d or 'hospShiftEnd' not in d or 
        'hId' not in d or 'patients' not in d):
        
        print('Insufficient or Incorrect Doctor Details .... please check \n\
               that all required fields in the dictionary are provided')

        raise Exception('InvalidDoctorDetails')
    
    if(d['dId'] in docDict):
        print('Entity with same ID exists')
        raise Exception('EntityPresentException')

    docDictAltered=True
    print('Posting details')
    newDoc=db.post('/Doctor/',docDetailsDict)
    print('Posted successfully')
    docDict[d['dId']]=newDoc['name']
    pickle.dump(docDict,open('Database/Binaries/DoctorID.bin','wb'))

def addHospital(hospDetailsDict):
    '''All details of the hospital must be supplied in the form of a dictionary
    stored in hospDetailsDict
    '''
    d=hospDetailsDict
    if('doctors' not in d or 'resourceToQuantity' not in d or 
        'hId' not in d or 'lat' not in d or 'long' not in d or
        'patients' not in d):

        print('Insufficient or Incorrect Hospital Details .... please check \n\
               that all required fields in the dictionary are provided')

        raise Exception('InvalidHospitalDetails')
    
    if(d['hId'] in hospDict):
        print('Entity with same ID exists')
        raise Exception('EntityPresentException')


    hospDictAltered=True
    print('Posting details')
    newHosp=db.post('/Hospital',hospDetailsDict)
    print('Posted successfully')
    hospDict[d['hId']]=newHosp['name']
    pickle.dump(hospDict,open('Database/Binaries/HospitalID.bin','wb'))
       

def addPatient(patDetailsDict):
    '''All details of the Patient must be supplied in the form of a dictionary
    stored in patDetailsDict
    '''
    d=patDetailsDict
    if('name' not in d or 'lat' not in d or 'long' not in d or
        'illnesses' not in d or 'isAdmitted' not in d or 
        'hId' not in d or 'pId' not in d or 'currentPrescriptions' not in d):

        print('Insufficient or Incorrect Patient Details .... please check \n\
               that all required fields in the dictionary are provided')

        raise Exception('InvalidPatientDetails')
    
    if(patDetailsDict['pId'] in patDict):
        print('Entity with the same ID exists')
        raise Exception('EntityPresentException')

    patDictAltered=True
    print('Posting details')
    newPat=db.post('/Patient',patDetailsDict)
    print('Posted successfully')
    patDict[d['pId']]=newPat['name']
    pickle.dump(patDict,open('Database/Binaries/PatientID.bin','wb'))
   

def addPrescription(prescDetailsDict):
    '''All details of the Prescription must be supplied in the form of a dictionary
    stored in prescDetailsDict
    '''
    d=prescDetailsDict
    if('prescId' not in d or 'dId' not in d or 'pId' not in d or 
        'additionalDetails' not in d):

        print('Insufficient or Incorrect Patient Details .... please check \n\
               that all required fields in the dictionary are provided')

        raise Exception('InvalidPatientDetails')
    
    if(d['prescId'] in prescDict):
        print("Entity with same ID exists")
        raise Exception('EntityPresentException')

    prescDictAltered=True
    print('Posting details')
    newPresc=db.post('/Prescription/',prescDetailsDict)
    print('Posted successfully')
    prescDict[d['prescId']]=newPresc['name']
    pickle.dump(prescDict,open('Database/Binaries/PrescriptionID.bin','wb'))
  
def hospGetPatients(hospId):
    actualId=hospDict[hospId]
    l=db.get('/Hospital/'+actualId,'patients')
    print('Patient IDs fetched ...')
    patDetails=list()
    for patId in l:
        actualPatId=patDict[patId]
        temp=db.get('/Patient',actualPatId)
        patDetails.append(temp)

    return patDetails

def docGetPatients(docId):
    actualId=docDict[docId]
    l=db.get('/Doctor/'+actualId,'patients')
    print('Patient IDs fetched')
    print(l)
    patDetails=list()
    for patId in l:
        actualPatId=patDict[patId]
        print(actualPatId)
        temp=db.get('/Patient',actualPatId)
        patDetails.append(temp)

    return patDetails


def patGetDoctors(patId):
    actualId=patDict[patId]
    l=db.get('/Patient/'+actualId,'currentPrescriptions')
    print('Prescription IDs fetched')
    docDetails=list()
    for prescId in l:
        actualPrescId=prescDict[prescId]
        docId=db.get('/Prescription/'+actualPrescId,'dId')
        actualDocId=docDict[docId]
        temp=db.get('/Doctor/'+actualDocId,None)
        print(temp)
        docDetails.append(temp)

    return docDetails

