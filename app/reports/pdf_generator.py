from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from reportlab.lib import colors

from app.reports.report_builder import ReportBuilder


class PDFGenerator:

    @staticmethod
    def generate(report, output_path):

        data = ReportBuilder.build(report)

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        doc = SimpleDocTemplate(output_path)

        styles = getSampleStyleSheet()

        elements = []

        # Title
        elements.append(Paragraph("<b>Digital Forensic Investigation Report</b>", styles["Title"]))

        # Case Information
        elements.append(Paragraph("<b>Case Information</b>", styles["Heading2"]))
        elements.append(Paragraph(f"Case Name: {data['case_name']}", styles["Normal"]))
        elements.append(Paragraph(f"Case Number: {data['case_number']}", styles["Normal"]))
        elements.append(Paragraph(f"Examiner: {data['examiner']}", styles["Normal"]))
        elements.append(Paragraph(f"Organization: {data['organization']}", styles["Normal"]))
        elements.append(Paragraph(f"Report Date: {data['report_date']}", styles["Normal"]))

        # Executive Summary
        elements.append(Paragraph("<b>Executive Summary</b>", styles["Heading2"]))
        elements.append(Paragraph(data["executive_summary"], styles["Normal"]))

        # Methodology
        elements.append(Paragraph("<b>Methodology</b>", styles["Heading2"]))
        elements.append(Paragraph(data["methodology"], styles["Normal"]))

        # Findings
        elements.append(Paragraph("<b>Findings</b>", styles["Heading2"]))
        for finding in data["findings"]:
            elements.append(Paragraph(f"• {finding}", styles["Normal"]))

        # Tool Versions
        elements.append(Paragraph("<b>Tool Versions</b>", styles["Heading2"]))

        tool_table = [["Tool", "Version"]]
        for tool in data["tool_versions"]:
            tool_table.append([tool["tool_name"], tool["version"]])

        table = Table(tool_table)
        table.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 6)
        ]))
        elements.append(table)

        # Hash Log
        elements.append(Paragraph("<b>Hash Log</b>", styles["Heading2"]))

        hash_table = [["File", "Algorithm", "Hash"]]
        for item in data["hash_log"]:
            hash_table.append([
                item["file_name"],
                item["algorithm"],
                item["hash_value"]
            ])

        table = Table(hash_table)
        table.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]))
        elements.append(table)

        # Chain of Custody
        elements.append(Paragraph("<b>Chain of Custody</b>", styles["Heading2"]))

        custody_table = [[
            "Evidence ID",
            "Collected By",
            "Collection Date",
            "Transferred To",
            "Transfer Date"
        ]]

        for item in data["chain_of_custody"]:
            custody_table.append([
                item["evidence_id"],
                item["collected_by"],
                item["collection_date"],
                item["transferred_to"],
                item["transfer_date"]
            ])

        table = Table(custody_table)
        table.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]))
        elements.append(table)

        # Evidence Appendix
        elements.append(Paragraph("<b>Evidence Appendix</b>", styles["Heading2"]))

        evidence_table = [["File", "Type", "Hash", "Metadata"]]

        for item in data["evidence_appendix"]:
            metadata = ", ".join(
                f"{k}: {v}" for k, v in item["metadata"].items()
            )

            evidence_table.append([
                item["file_name"],
                item["file_type"],
                item["hash_value"],
                metadata
            ])

        table = Table(evidence_table)
        table.setStyle(TableStyle([
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ]))
        elements.append(table)

        doc.build(elements)

        return output_path