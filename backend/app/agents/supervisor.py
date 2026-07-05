from app.memory.context import AgentContext

from app.agents.mutation_agent import MutationAgent


class SupervisorAgent:

    def __init__(self):

        self.pipeline = [

            MutationAgent(),

        ]

    def execute(self, genes):

        context = AgentContext()

        context["genes"] = genes

        for agent in self.pipeline:

            print(f"Running {agent.name}")

            context = agent.run(context)

        return context