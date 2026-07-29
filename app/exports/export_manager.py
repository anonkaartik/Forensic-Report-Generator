from pathlib import Path

from jinja2 import Environment, FileSystemLoader

from app.reports.report_builder import ReportBuilder


class ExportManager:

    @staticmethod
    def export_html(report, output_path):

        data = ReportBuilder.build(report)

        env = Environment(
            loader=FileSystemLoader("app/templates")
        )

        template = env.get_template("report_template.html")

        html = template.render(**data)

        Path(output_path).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(html)

        return output_path