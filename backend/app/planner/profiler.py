import time


class PipelineProfiler:

    def __init__(self):
        self.timings = {}

    def reset(self):
        self.timings = {}

    def start(self, name):
        self.timings[name] = {
            "start": time.perf_counter()
        }

    def stop(self, name):
        if name in self.timings:
            self.timings[name]["elapsed"] = (
                time.perf_counter()
                - self.timings[name]["start"]
            )

    def report(self):

        print("\n")
        print("=" * 60)
        print("PIPELINE PROFILE")
        print("=" * 60)

        total = 0.0

        for agent, data in self.timings.items():

            elapsed = data.get("elapsed")

            if elapsed is None:
                print(f"{agent:30}SKIPPED")
                continue

            total += elapsed

            print(
                f"{agent:30}{elapsed:.2f} sec"
            )

        print("-" * 60)
        print(
            f"{'TOTAL':30}{total:.2f} sec"
        )