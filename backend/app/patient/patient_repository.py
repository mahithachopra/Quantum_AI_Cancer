class PatientRepository:

    def __init__(self):

        self.patients = {}

    def add(self, patient):

        self.patients[patient.patient_id] = patient

    def get(self, patient_id):

        return self.patients.get(patient_id)