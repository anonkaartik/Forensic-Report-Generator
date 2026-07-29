import os

from flask import Flask, render_template, request

from app.ingestion.json_adapter import JSONAdapter
from app.ingestion.csv_adapter import CSVAdapter

from app.reports.pdf_generator import PDFGenerator
from app.exports.export_manager import ExportManager
from app.exports.docx_export import DOCXExport

from app.signatures.digital_signature import DigitalSignature

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

UPLOAD_FOLDER = "data/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    if "file" not in request.files:
        return "No file uploaded."

    uploaded_file = request.files["file"]

    if uploaded_file.filename == "":
        return "No file selected."

    file_path = os.path.join(
        UPLOAD_FOLDER,
        uploaded_file.filename
    )

    uploaded_file.save(file_path)

    extension = uploaded_file.filename.rsplit(".", 1)[-1].lower()

    if extension == "json":
        report = JSONAdapter.load(file_path)

    elif extension == "csv":
        report = CSVAdapter.load(file_path)

    else:
        return "Unsupported file type."

    PDFGenerator.generate(
        report,
        "output/pdf/report.pdf"
    )

    ExportManager.export_html(
        report,
        "output/html/report.html"
    )

    DOCXExport.export(
        report,
        "output/docx/report.docx"
    )

    private_key = "output/keys/private.pem"
    public_key = "output/keys/public.pem"

    if not os.path.exists(private_key):
        DigitalSignature.generate_keys(
            private_key,
            public_key
        )

    DigitalSignature.sign_file(
        "output/pdf/report.pdf",
        private_key,
        "output/pdf/report.sig"
    )

    return render_template(
        "success.html",
        pdf="output/pdf/report.pdf",
        html="output/html/report.html",
        docx="output/docx/report.docx"
    )


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )