from dataclasses import asdict


class JSONRenderer:

    def render(self, report):

        return asdict(report)