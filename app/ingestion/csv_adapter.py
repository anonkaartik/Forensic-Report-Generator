import csv
from app.reports.report_schema import (
    ForensicReport,
    HashRecord,
    EvidenceItem
)


class CSVAdapter:

    @staticmethod
    def load(file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            reader = list(csv.DictReader(file))

        if not reader:
            raise ValueError("CSV file is empty.")

        first = reader[0]

        report = ForensicReport(
            case_name=first["case_name"],
            case_number=first["case_number"],
            examiner=first["examiner"],
            organization=first["organization"],
            report_date=first["report_date"],
            executive_summary=first["executive_summary"],
            methodology=first["methodology"]
        )

        for row in reader:

            report.hash_log.append(
                HashRecord(
                    row["file_name"],
                    row["algorithm"],
                    row["hash_value"]
                )
            )

            report.evidence_appendix.append(
                EvidenceItem(
                    row["file_name"],
                    row["file_type"],
                    row["hash_value"],
                    {
                        "Size": row["size"],
                        "Format": row["format"]
                    }
                )
            )

        return report