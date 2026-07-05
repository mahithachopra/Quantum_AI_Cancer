from dataclasses import dataclass, field

from typing import List

from app.planner.task import Task


@dataclass
class Workflow:

    name: str

    description: str = ""

    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task):

        self.tasks.append(task)

    def ordered_tasks(self):

        return sorted(

            self.tasks,

            key=lambda t: t.priority

        )