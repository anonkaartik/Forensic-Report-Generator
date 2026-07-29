from app.reports.report_schema import ForensicReport


class ReportBuilder:

    @staticmethod
    def build(report: ForensicReport):

        return {
            "case_name": report.case_name,
            "case_number": report.case_number,
            "examiner": report.examiner,
            "organization": report.organization,
            "report_date": report.report_date,
            "executive_summary": report.executive_summary,
            "methodology": report.methodology,
            "findings": report.findings,

            "tool_versions": [
                {
                    "tool_name": tool.tool_name,
                    "version": tool.version
                }
                for tool in report.tool_versions
            ],

            "hash_log": [
                {
                    "file_name": item.file_name,
                    "algorithm": item.algorithm,
                    "hash_value": item.hash_value
                }
                for item in report.hash_log
            ],

            "chain_of_custody": [
                {
                    "evidence_id": item.evidence_id,
                    "collected_by": item.collected_by,
                    "collection_date": item.collection_date,
                    "transferred_to": item.transferred_to,
                    "transfer_date": item.transfer_date
                }
                for item in report.chain_of_custody
            ],

            "evidence_appendix": [
                {
                    "file_name": item.file_name,
                    "file_type": item.file_type,
                    "hash_value": item.hash_value,
                    "metadata": item.metadata
                }
                for item in report.evidence_appendix
            ]
        }