class AgentRegistry:

    def __init__(self):
        self._agents = {}

    def register(self, agent):
        self._agents[agent.name] = agent

    def get(self, name):
        return self._agents.get(name)

    def unregister(self, name):
        self._agents.pop(name, None)

    def list_agents(self):
        return list(self._agents.keys())

    def clear(self):
        self._agents.clear()