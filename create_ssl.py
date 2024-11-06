# create_ssl.py
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from datetime import datetime, timedelta
import ipaddress

# Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Generate public key
public_key = private_key.public_key()

# Create a self-signed certificate
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"EU"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"---"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"---"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"Map-IT"),
        x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, u"IT"),

    x509.NameAttribute(NameOID.COMMON_NAME, u"localhost"),
])
cert = x509.CertificateBuilder().subject_name(
    subject
).issuer_name(
    issuer
).public_key(
    public_key
).serial_number(
    x509.random_serial_number()
).not_valid_before(
    datetime.utcnow()
).not_valid_after(
    # Certificate is valid for 1 year
    datetime.utcnow() + timedelta(days=365)
).add_extension(
    x509.SubjectAlternativeName([
        x509.DNSName(u"localhost"),
        x509.IPAddress(ipaddress.IPv4Address("127.0.0.1")),
    ]),
    critical=False,
).sign(private_key, hashes.SHA256())

# Write the private key to a file
with open("./frontend/ssl/key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=Encoding.PEM,
        format=PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=NoEncryption(),
    ))

# Write the certificate to a file
with open("./frontend/ssl/cert.pem", "wb") as f:
    f.write(cert.public_bytes(Encoding.PEM))