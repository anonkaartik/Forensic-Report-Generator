from app.ingestion.json_adapter import JSONAdapter
from app.reports.report_builder import ReportBuilder

report = JSONAdapter.load("data/json/sample_case.json")

data = ReportBuilder.build(report)

print(data)