from app.memory import AgentSession
from app.graph.graph_service import GraphService
from app.representation.representation_service import RepresentationService

session = AgentSession()

session.context.genes = [

    "EGFR",

    "TP53",

    "PIK3CA"

]

session.context.graph_analysis = GraphService().analyze(

    session.context.genes

)

repo = RepresentationService().build(

    session.context

)

for entity in repo.all():

    print(entity.name)

    print(entity.entity_type)

    print(entity.graph_features.keys())