# Forensic Report Generator

## Overview

The Forensic Report Generator is an automated digital forensic reporting platform developed as part of an internship project. The system generates professional forensic investigation reports by processing evidence collected from forensic tools and organizing it according to established forensic reporting standards.

The project follows the reporting guidelines of:

- SWGDE (Scientific Working Group on Digital Evidence)
- ACPO (Association of Chief Police Officers)
- ISO/IEC 27037

The generated reports include all essential forensic documentation such as findings, methodology, chain of custody, hash logs, examiner certification, and evidence appendices.

---

## Objectives

- Generate automated forensic investigation reports.
- Support JSON and CSV evidence input.
- Produce court-ready PDF reports.
- Generate DOCX and HTML versions of reports.
- Include digital signature support for examiner certification.
- Follow SWGDE, ACPO, and ISO/IEC 27037 reporting standards.

---

## Features

- Automated forensic report generation
- Three professional report templates
- JSON data ingestion
- CSV data ingestion
- Executive summary generation
- Methodology section
- Tool version documentation
- Findings section
- Hash log generation
- Chain of custody documentation
- Evidence appendix generation
- RSA/X.509 digital signature integration
- PDF export
- DOCX export
- HTML export

---

## Technology Stack

- Python 3
- Flask
- Jinja2
- ReportLab
- WeasyPrint
- PyPDF2
- Cryptography
- python-docx
- Pandas

---

## Project Structure

```text
Forensic-Report-Generator/
│
├── app/
│   ├── exports/
│   ├── ingestion/
│   ├── reports/
│   ├── signatures/
│   ├── templates/
│   └── utils/
│
├── data/
│   ├── csv/
│   └── json/
│
├── docs/
├── output/
│   ├── docx/
│   ├── html/
│   └── pdf/
│
├── tests/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Team Members

| Member | Role | Responsibilities |
|----------|------|------------------|
| Kaartik | Project Lead & Full-Stack Developer | Project architecture, report generation engine, template development, module integration, testing, GitHub repository management |
| Anant | Data Processing & Evidence Management | Report schema planning, JSON/CSV mapping, evidence organization, report validation |
| Kush | Documentation & Quality Assurance | Documentation, report review, standards verification, testing support, presentation preparation |

---

## Expected Outputs

- PDF forensic report
- DOCX forensic report
- HTML forensic report

---

## Standards Followed

- SWGDE Best Practices
- ACPO Good Practice Guide
- ISO/IEC 27037

---

## Installation

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run the application.

```bash
python app.py
```

---

## License

This project was developed as part of an internship for educational purposes.