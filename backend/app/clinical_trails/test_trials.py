from app.clinical_trials.clinical_trial_service import ClinicalTrialService

service = ClinicalTrialService()

trials = service.search([
    {
        "gene": "EGFR",
        "drug": "Osimertinib"
    }
])

print(len(trials))

for t in trials[:5]:

    print()

    print("NCT:", t.nct_id)

    print("Title:", t.title)

    print("Status:", t.status)

    print("Phase:", t.phase)

    print("Condition:", t.condition)

    print("Drug:", t.intervention)

    print("URL:", t.url)