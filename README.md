# Forensic Report Generator

A Python and Flask based application for generating professional digital forensic investigation reports. The application accepts forensic evidence data in JSON and CSV formats, structures the information according to a standardized report format, generates reports in PDF, HTML, and DOCX formats, and digitally signs the generated PDF using RSA cryptography.

---

## Features

- JSON Evidence Parsing
- CSV Evidence Parsing
- Automated Report Generation
- PDF Report Export
- HTML Report Export
- DOCX Report Export
- RSA Digital Signature
- Modular Project Architecture
- Flask Web Interface

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Flask | Web Framework |
| Jinja2 | HTML Template Rendering |
| ReportLab | PDF Generation |
| python-docx | DOCX Generation |
| Cryptography | Digital Signature |
| HTML | User Interface |
| CSS | Styling |

---

## Project Structure

```
Forensic-Report-Generator/

├── app/
│   ├── exports/
│   ├── ingestion/
│   ├── reports/
│   ├── signatures/
│   ├── static/
│   └── templates/
│
├── data/
├── docs/
├── output/
├── tests/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Open the project folder.

Install dependencies.

```bash
pip install flask
pip install reportlab
pip install python-docx
pip install cryptography
pip install jinja2
```

or

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application.

```bash
python app.py
```

Open the browser.

```
http://127.0.0.1:5000
```

---

## Input

Supported input formats:

- JSON
- CSV

The uploaded file should contain forensic investigation data such as:

- Case Information
- Executive Summary
- Methodology
- Findings
- Tool Versions
- Hash Logs
- Chain of Custody
- Evidence Appendix

---

## Output

The application generates:

```
output/

pdf/
    report.pdf
    report.sig

html/
    report.html

docx/
    report.docx
```

---

## Workflow

1. Upload a JSON or CSV evidence file.
2. Parse the uploaded data.
3. Build the forensic report.
4. Generate PDF report.
5. Generate HTML report.
6. Generate DOCX report.
7. Digitally sign the PDF report.
8. Save generated reports to the output directory.

---

## Project Modules

### JSON Adapter

Reads and parses forensic investigation data stored in JSON format.

### CSV Adapter

Reads and parses forensic investigation data stored in CSV format.

### Report Builder

Converts parsed data into a structured forensic report.

### PDF Generator

Generates forensic reports in PDF format using ReportLab.

### HTML Export

Generates HTML reports using Jinja2 templates.

### DOCX Export

Creates Microsoft Word reports using python-docx.

### Digital Signature

Generates RSA keys and digitally signs PDF reports.

### Flask Application

Provides the web interface for uploading files and generating reports.

---

## Documentation

Project documentation is available in the `docs/` directory.

- Project Report
- User Guide
- Installation Guide
- Technical Documentation

---

## Future Enhancements

- Database Integration
- User Authentication
- Cloud Deployment
- Case Management
- Additional Report Templates
- Automated Evidence Verification

---

## Author

Internship Project

Forensic Report Generator

Developed using Python, Flask, ReportLab, Jinja2, python-docx, and Cryptography.

---

## License

This project has been developed for educational and internship purposes.