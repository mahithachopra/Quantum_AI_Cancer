from app.patient.patient import Patient


class PatientBuilder:

    def build(self, context, entity_repository):

        patient = Patient(
            patient_id="DemoPatient"
        )

        patient.genes = entity_repository.all()

        patient.pathways = context.pathway_analysis

        patient.literature = context.literature

        patient.evidence = context.evidence

        patient.trials = context.clinical_trials

        patient.drugs = context.recommendations

        return patient