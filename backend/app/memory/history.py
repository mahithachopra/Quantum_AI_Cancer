from datetime import datetime


class ExecutionHistory:

    def __init__(self):

        self.records = []

    def add(

        self,

        agent,

        status,

        execution_time

    ):

        self.records.append(

            {

                "agent": agent,

                "status": status,

                "time": execution_time,

                "timestamp": datetime.now().isoformat()

            }

        )

    def all(self):

        return self.records