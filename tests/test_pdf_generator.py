from app.ingestion.json_adapter import JSONAdapter
from app.reports.pdf_generator import PDFGenerator

report = JSONAdapter.load(
    "data/json/sample_case.json"
)

output = PDFGenerator.generate(
    report,
    "output/pdf/sample_report.pdf"
)

print("PDF generated successfully.")
print(output)