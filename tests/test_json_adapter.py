from app.ingestion.json_adapter import JSONAdapter

report = JSONAdapter.load("data/json/sample_case.json")

print(report)
