from app.reports.report_schema import (
    ForensicReport,
    ToolVersion,
    HashRecord,
    ChainOfCustody,
    EvidenceItem
)

report = ForensicReport(
    case_name="Case-001",
    case_number="FRG-001",
    examiner="Kaartik",
    organization="Internship Project",
    report_date="29-07-2026",
    executive_summary="This is a sample executive summary.",
    methodology="Evidence collected according to ISO/IEC 27037."
)

report.tool_versions.append(
    ToolVersion("Autopsy", "4.21")
)

report.hash_log.append(
    HashRecord("disk.img", "SHA256", "ABC123")
)

report.chain_of_custody.append(
    ChainOfCustody(
        "EV-001",
        "Kaartik",
        "29-07-2026",
        "Forensic Lab",
        "29-07-2026"
    )
)

report.evidence_appendix.append(
    EvidenceItem(
        "disk.img",
        "Disk Image",
        "ABC123",
        {
            "Size": "10 GB",
            "Format": "E01"
        }
    )
)

print(report)