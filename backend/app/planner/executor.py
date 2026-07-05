from app.planner.dependency_resolver import DependencyResolver
from app.planner.cache_manager import CacheManager
from app.planner.profiler import PipelineProfiler


class WorkflowExecutor:

    def __init__(

        self,

        registry

    ):

        self.registry = registry

        self.resolver = DependencyResolver()

        self.cache = CacheManager()
        self.profiler = PipelineProfiler()

    def execute(

        self,

        workflow,

        context

    ):
        self.profiler.reset()
        self.resolver.validate(

            workflow

        )

        for task in workflow.ordered_tasks():

            print(

                f"Running {task.agent}"

            )
            self.profiler.start(task.agent)

            agent = self.registry.get(task.agent)

            #
            # Skip if result already exists in memory
            #

            if self.cache.has_result(

                context,

                task.agent

            ):

                print(

                    f"Skipping {task.agent} (cached)"

                )

                continue

            agent = self.registry.get(

                task.agent

            )

            if agent is None:

                raise RuntimeError(

                    f"{task.agent} not registered."

                )

            context.current_agent = task.agent

            task.status = task.status.RUNNING

            context = agent.run(

                context

            )
            self.profiler.stop(task.agent)

            print(
                f"Completed {task.agent}"
            )

            task.status = task.status.SUCCESS

        self.profiler.report()

        return context