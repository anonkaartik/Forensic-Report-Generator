from app.ingestion.json_adapter import JSONAdapter
from app.exports.export_manager import ExportManager

report = JSONAdapter.load(
    "data/json/sample_case.json"
)

output = ExportManager.export_html(
    report,
    "output/html/sample_report.html"
)

print("HTML generated successfully.")
print(output)