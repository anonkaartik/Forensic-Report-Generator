from app.ingestion.json_adapter import JSONAdapter
from app.exports.docx_export import DOCXExport

report = JSONAdapter.load(
    "data/json/sample_case.json"
)

output = DOCXExport.export(
    report,
    "output/docx/sample_report.docx"
)

print("DOCX generated successfully.")
print(output)