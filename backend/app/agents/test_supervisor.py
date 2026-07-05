from pprint import pprint

from app.agents.supervisor import SupervisorAgent

supervisor = SupervisorAgent()

context = supervisor.execute(

    [

        "EGFR",

        "TP53",

        "PIK3CA"

    ]

)

pprint(context)