from abc import ABC, abstractmethod


class BaseAgent(ABC):

    name = "BaseAgent"

    description = ""

    @abstractmethod
    def run(self, context: dict):

        """
        Receives the shared context.

        Updates the context.

        Returns context.
        """

        pass