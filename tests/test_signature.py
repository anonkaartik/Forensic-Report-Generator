from app.signatures.digital_signature import DigitalSignature

DigitalSignature.generate_keys(
    "output/keys/private.pem",
    "output/keys/public.pem"
)

DigitalSignature.sign_file(
    "output/pdf/sample_report.pdf",
    "output/keys/private.pem",
    "output/pdf/sample_report.sig"
)

verified = DigitalSignature.verify_file(
    "output/pdf/sample_report.pdf",
    "output/keys/public.pem",
    "output/pdf/sample_report.sig"
)

print("Signature Verified:", verified)