# app/report/json_renderer.py

from dataclasses import asdict


class JSONRenderer:

    def render(self, report):

        return asdict(report)