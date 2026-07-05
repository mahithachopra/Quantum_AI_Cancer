class HTMLRenderer:

    def render(self, report):

        html = f"""
        <html>

        <head>

        <title>Precision Oncology Report</title>

        </head>

        <body>

        <h1>Precision Oncology Report</h1>

        <h2>Detected Genes</h2>

        <ul>
        """

        for gene in report.genes:

            html += f"<li>{gene}</li>"

        html += "</ul>"

        html += "<h2>Recommendations</h2><ul>"

        for recommendation in report.recommendations:

            html += f"""

            <li>

            <b>{recommendation.drug}</b>

            ({recommendation.confidence:.2f})

            </li>

            """

        html += "</ul>"

        html += "</body></html>"

        return html