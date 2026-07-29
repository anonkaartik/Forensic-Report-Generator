# INSTALLATION GUIDE

## Forensic Report Generator

---

# Introduction

This guide explains how to install, configure, and run the Forensic Report Generator application on a Windows system.

---

# Prerequisites

Before installing the project, ensure the following software is available:

- Windows 10 or Windows 11
- Python 3.x
- Git
- Visual Studio Code

---

# Project Structure

```
Forensic-Report-Generator/

│
├── app/
├── data/
├── docs/
├── output/
├── tests/
├── app.py
├── requirements.txt
└── README.md
```

---

# Step 1: Download the Project

Clone the repository.

```bash
git clone <repository-url>
```

Or download the ZIP file and extract it.

---

# Step 2: Open the Project

Open Visual Studio Code.

Select

```
File → Open Folder
```

Choose the project directory.

---

# Step 3: Create Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it.

Windows

```bash
venv\Scripts\activate
```

---

# Step 4: Install Dependencies

Install all required Python packages.

```bash
pip install flask
pip install reportlab
pip install python-docx
pip install cryptography
pip install jinja2
```

Or install everything together if a requirements file is available.

```bash
pip install -r requirements.txt
```

---

# Step 5: Verify Folder Structure

Ensure the following folders exist.

```
data/uploads/

output/pdf/

output/html/

output/docx/

output/keys/
```

Create any missing folders before running the project.

---

# Step 6: Start the Application

Open the terminal.

Run:

```bash
python app.py
```

The Flask development server starts.

Example:

```
Running on http://127.0.0.1:5000
```

---

# Step 7: Open the Application

Open any web browser.

Visit:

```
http://127.0.0.1:5000
```

The home page of the application appears.

---

# Step 8: Upload Evidence File

Choose either:

- JSON file

or

- CSV file

Click

```
Generate Report
```

---

# Step 9: Generated Reports

After successful execution, reports are stored inside:

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

# Common Installation Problems

## Python Not Found

Check installation.

```bash
python --version
```

---

## Missing Package

Install the missing library.

Example:

```bash
pip install reportlab
```

---

## Flask Not Starting

Run:

```bash
python app.py
```

Verify that all dependencies are installed.

---

## Module Not Found

Install the missing package using pip.

---

## Permission Error

Run Visual Studio Code as Administrator if required.

---

# Uninstallation

Delete the project folder.

If a virtual environment was created, delete the

```
venv/
```

folder.

---

# Installation Complete

The application is now ready for forensic report generation.