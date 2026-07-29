from pathlib import Path

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization


class DigitalSignature:

    @staticmethod
    def generate_keys(private_key_path, public_key_path):

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )

        public_key = private_key.public_key()

        Path(private_key_path).parent.mkdir(parents=True, exist_ok=True)

        with open(private_key_path, "wb") as f:
            f.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )

        with open(public_key_path, "wb") as f:
            f.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

    @staticmethod
    def sign_file(file_path, private_key_path, signature_path):

        with open(private_key_path, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None
            )

        with open(file_path, "rb") as f:
            data = f.read()

        signature = private_key.sign(
            data,
            padding.PKCS1v15(),
            hashes.SHA256()
        )

        with open(signature_path, "wb") as f:
            f.write(signature)

    @staticmethod
    def verify_file(file_path, public_key_path, signature_path):

        with open(public_key_path, "rb") as f:
            public_key = serialization.load_pem_public_key(
                f.read()
            )

        with open(file_path, "rb") as f:
            data = f.read()

        with open(signature_path, "rb") as f:
            signature = f.read()

        try:
            public_key.verify(
                signature,
                data,
                padding.PKCS1v15(),
                hashes.SHA256()
            )

            return True

        except Exception:
            return False