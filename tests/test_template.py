from jinja2 import Environment, FileSystemLoader

from app.ingestion.json_adapter import JSONAdapter
from app.reports.report_builder import ReportBuilder

report = JSONAdapter.load("data/json/sample_case.json")

data = ReportBuilder.build(report)

env = Environment(loader=FileSystemLoader("app/templates"))

template = env.get_template("report_template.html")

html = template.render(**data)

print(html)