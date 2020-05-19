from Database import ManageDB

def addPatient():
    pat={
        'name':'Shayak',
        'lat':70,
        'long':85,
        'illnesses':['PRESC1','PRESC100','PRES10'],
        'isAdmitted':False,
        'hId':'hosnull',
        'pId':'PAT20',
        'currentPrescriptions':['PREC1001','PRES1','PRESC9']
        }

    ManageDB.addPatient(pat);

def addHospital():
    hosp={
        'doctors':['DOC100','DOC200','DOC300'],
        'resourceToQuantity':{'RES1':100,'RES2':200,'RES3':300},
        'hId':'HOSP200',
        'lat':66,
        'long':40,
        'patients':['PAT100','PAT1','PAT20']
        }
    ManageDB.addHospital(hosp)

def addDoctor():
    doc={
        'dId':'DOC200',
        'name':'Dr. House',
        'visStart':2000,
        'visEnd':2200,
        'lat':20,
        'long':100,
        'hospShiftStart':600,
        'hospShiftEnd':1800,
        'hId':'HOSP100',
        'patients':['PAT1','PAT20']
        }
    ManageDB.addDoctor(doc)

def addPrescription():
    presc={
            'prescId':'PRESC9',
            'dId':'DOC100',
            'pId':'PAT100',
            'additionalDetails':{
                    'med1':'azithromycin',
                    'med2':'calpol',
                    'med3':'cocaine...lots of it'
                    }
            }
    ManageDB.addPrescription(presc)

#addPrescription()
#exit(0)
details=ManageDB.patGetDoctors('PAT100')
print(details)
ManageDB.closeModule()
