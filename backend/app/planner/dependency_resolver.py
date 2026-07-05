class DependencyResolver:

    def validate(self, workflow):

        completed = set()

        for task in workflow.ordered_tasks():

            missing = [

                dependency

                for dependency in task.depends_on

                if dependency not in completed

            ]

            if missing:

                raise RuntimeError(

                    f"{task.name} is missing dependencies: {missing}"

                )

            completed.add(task.name)

        return True