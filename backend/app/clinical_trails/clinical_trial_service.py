from concurrent.futures import ThreadPoolExecutor

from app.clinical_trials.clinicaltrials_client import ClinicalTrialsClient
from app.clinical_trials.models import ClinicalTrial


class ClinicalTrialService:

    def __init__(self):
        self.client = ClinicalTrialsClient()

    def search(
        self,
        recommendations,
        max_results=5
    ):

        trials = []

        with ThreadPoolExecutor(max_workers=5) as executor:

            futures = {}

            for recommendation in recommendations[:max_results]:

                future = executor.submit(
                    self.client.search,
                    recommendation["gene"],
                    recommendation["drug"]
                )

                futures[future] = recommendation

            for future, recommendation in futures.items():

                try:
                    studies = future.result()

                except Exception:
                    continue

                for study in studies:

                    protocol = study.get(
                        "protocolSection",
                        {}
                    )

                    ident = protocol.get(
                        "identificationModule",
                        {}
                    )

                    status = protocol.get(
                        "statusModule",
                        {}
                    )

                    design = protocol.get(
                        "designModule",
                        {}
                    )

                    conditions = protocol.get(
                        "conditionsModule",
                        {}
                    )

                    arms = protocol.get(
                        "armsInterventionsModule",
                        {}
                    )

                    trials.append(

                        ClinicalTrial(

                            gene=recommendation["gene"],

                            drug=recommendation["drug"],

                            nct_id=ident.get(
                                "nctId",
                                ""
                            ),

                            title=ident.get(
                                "briefTitle",
                                ""
                            ),

                            status=status.get(
                                "overallStatus",
                                ""
                            ),

                            phase=", ".join(
                                design.get(
                                    "phases",
                                    []
                                )
                            ),

                            condition=", ".join(
                                conditions.get(
                                    "conditions",
                                    []
                                )
                            ),

                            intervention=", ".join(
                                [
                                    item.get("name", "")
                                    for item in arms.get(
                                        "interventions",
                                        []
                                    )
                                ]
                            ),

                            country="Multiple",

                            url=f"https://clinicaltrials.gov/study/{ident.get('nctId','')}"

                        )

                    )

        return trials