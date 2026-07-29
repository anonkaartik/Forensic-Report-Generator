from app.ingestion.csv_adapter import CSVAdapter

report = CSVAdapter.load("data/csv/sample_case.csv")

print(report)