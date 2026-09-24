class Patient:

    def __init__(self, patient_id, sex, age , status,
                 apoe, thal, ttau, abeta40, abeta42, ptau):
    
        self.patient_id = patient_id
        self.sex = sex
        self. age = age
        self.status = status
        self.apoe = apoe
        self.thal = thal
        self.ttau = ttau
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ptau = ptau
        

    def __repr__(self):
        return f"Patient {self.patient_id}: {self.age}, {self.sex}, {self.status}"

    @classmethod
    def find_and_select_patients(cls, patients):
     
        print("Patients that I selected here that smiliar to my conditions:")

        for patient in patients:
            if  patient.sex == "Female" and patient.status == "Dementia":
                print(patient)