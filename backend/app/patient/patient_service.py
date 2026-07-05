from app.patient.patient_builder import PatientBuilder
from app.patient.patient_repository import PatientRepository


class PatientService:

    def __init__(self):

        self.builder = PatientBuilder()

        self.repository = PatientRepository()

    def create(

        self,

        context,

        entity_repository

    ):

        patient = self.builder.build(

            context,

            entity_repository

        )

        self.repository.add(patient)

        return patient