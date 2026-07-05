from app.registry.agent_registry import AgentRegistry
from app.registry.agent_factory import AgentFactory


class RegistryLoader:

    def load(self):

        registry = AgentRegistry()

        agents = [

    "Mutation Agent",

    "Graph Agent",

    "Drug Agent",

    "Pathway Agent",

    "Evidence Agent",

    "Literature Agent",

    "Clinical Trial Agent",

    "Evidence Fusion Agent",
    "Explainability Agent",
    "Report Agent",

]
        for agent_name in agents:

            try:

                agent = AgentFactory.create(agent_name)

                registry.register(agent)

            except Exception as e:

                print(f"Skipping {agent_name}: {e}")

        return registry