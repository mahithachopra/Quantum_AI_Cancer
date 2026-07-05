class TrialRanker:

    STATUS = {

        "RECRUITING": 1.0,

        "ACTIVE, NOT RECRUITING": 0.9,

        "NOT YET RECRUITING": 0.8,

        "COMPLETED": 0.5

    }

    def rank(self, trials):

        for trial in trials:

            trial.score = self.STATUS.get(
                trial.status.upper(),
                0.3
            )

        trials.sort(
            key=lambda x: x.score,
            reverse=True
        )

        return trials