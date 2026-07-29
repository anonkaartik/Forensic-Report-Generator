# USER GUIDE

## Forensic Report Generator

---

# Introduction

The Forensic Report Generator is a web-based application developed using Python and Flask. It automates the process of generating digital forensic reports from investigation data stored in JSON or CSV files.

The application generates reports in multiple formats including PDF, HTML, and DOCX, and digitally signs the PDF report for authenticity.

---

# System Requirements

## Hardware

- Processor: Intel Core i3 or above
- RAM: 4 GB minimum
- Storage: 500 MB free space

## Software

- Windows 10/11
- Python 3.x
- Visual Studio Code
- Git

---

# Starting the Application

Open the project folder in Visual Studio Code.

Open the terminal.

Run the application:

```bash
python app.py
```

The Flask server starts.

Open the browser.

Visit:

```
http://127.0.0.1:5000
```

---

# Home Page

The home page provides:

- Project title
- Upload form
- File selection
- Generate Report button

---

# Uploading Evidence

Click **Choose File**.

Select either:

- JSON file
- CSV file

Only supported forensic evidence files should be uploaded.

---

# Generating Reports

After selecting the file:

Click

```
Generate Report
```

The application automatically:

- Reads the uploaded file.
- Builds the forensic report.
- Generates PDF report.
- Generates HTML report.
- Generates DOCX report.
- Creates a digital signature.

---

# Output Location

Generated reports are stored inside:

```
output/
```

The directory contains:

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

# Report Contents

Each report contains:

- Case Information
- Executive Summary
- Methodology
- Findings
- Tool Versions
- Hash Log
- Chain of Custody
- Evidence Appendix

---

# Supported File Types

Input:

- JSON
- CSV

Output:

- PDF
- HTML
- DOCX
- Digital Signature (.sig)

---

# Troubleshooting

## Flask server not starting

Run:

```bash
python app.py
```

Check whether Flask is installed.

---

## Unsupported file type

Ensure that only JSON or CSV files are uploaded.

---

## Report not generated

Verify that the uploaded file follows the expected forensic report structure.

---

## Missing Python packages

Install dependencies using:

```bash
pip install flask reportlab python-docx cryptography jinja2
```

---

# Best Practices

- Always validate forensic evidence before uploading.
- Keep generated reports in a secure location.
- Protect the generated RSA private key.
- Verify the digital signature before sharing reports.

---

# End of User Guide