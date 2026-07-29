import json
from app.reports.report_schema import (
    ForensicReport,
    ToolVersion,
    HashRecord,
    ChainOfCustody,
    EvidenceItem
)


class JSONAdapter:

    @staticmethod
    def load(file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        report = ForensicReport(
            case_name=data["case_name"],
            case_number=data["case_number"],
            examiner=data["examiner"],
            organization=data["organization"],
            report_date=data["report_date"],
            executive_summary=data["executive_summary"],
            methodology=data["methodology"]
        )

        for tool in data.get("tool_versions", []):
            report.tool_versions.append(
                ToolVersion(
                    tool["tool_name"],
                    tool["version"]
                )
            )

        for item in data.get("hash_log", []):
            report.hash_log.append(
                HashRecord(
                    item["file_name"],
                    item["algorithm"],
                    item["hash_value"]
                )
            )

        for item in data.get("chain_of_custody", []):
            report.chain_of_custody.append(
                ChainOfCustody(
                    item["evidence_id"],
                    item["collected_by"],
                    item["collection_date"],
                    item["transferred_to"],
                    item["transfer_date"]
                )
            )

        for item in data.get("evidence_appendix", []):
            report.evidence_appendix.append(
                EvidenceItem(
                    item["file_name"],
                    item["file_type"],
                    item["hash_value"],
                    item["metadata"]
                )
            )

        report.findings.extend(data.get("findings", []))

        return report