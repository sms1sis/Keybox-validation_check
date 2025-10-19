import requests
import sys
import xml.etree.ElementTree as ET
from cryptography import x509

# ANSI color codes for pretty output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

print(f"{CYAN}{BOLD}\n🔍 Checking Android Keybox Status...{RESET}")

# Fetch CRL data
try:
    print(f"{YELLOW}→ Fetching revocation list from Google...{RESET}")
    crl = requests.get('https://android.googleapis.com/attestation/status').json()
    print(f"{GREEN}✔ Revocation list loaded successfully.{RESET}")
except Exception as e:
    print(f"{RED}✖ Failed to fetch CRL: {e}{RESET}")
    sys.exit(1)

# Parse XML input file
try:
    print(f"{YELLOW}→ Parsing XML file: {sys.argv[1]}{RESET}")
    certs = [elem.text for elem in ET.parse(sys.argv[1]).getroot().iter() if elem.text and "BEGIN CERTIFICATE" in elem.text]
except Exception as e:
    print(f"{RED}✖ Failed to parse XML: {e}{RESET}")
    sys.exit(1)

def parse_cert(cert):
    cert = "\n".join(line.strip() for line in cert.strip().split("\n"))
    parsed = x509.load_pem_x509_certificate(cert.encode())
    return f"{parsed.serial_number:x}"

# Extract EC and RSA serial numbers
try:
    ec_cert_sn, rsa_cert_sn = parse_cert(certs[0]), parse_cert(certs[3])
except Exception as e:
    print(f"{RED}✖ Failed to parse certificates: {e}{RESET}")
    sys.exit(1)

print(f"\n{BOLD}Certificate Serial Numbers:{RESET}")
print(f"  🔹 EC  Cert SN: {CYAN}{ec_cert_sn}{RESET}")
print(f"  🔹 RSA Cert SN: {CYAN}{rsa_cert_sn}{RESET}")

# Check revocation
revoked = any(sn in crl.get("entries", {}).keys() for sn in (ec_cert_sn, rsa_cert_sn))

if revoked:
    print(f"\n{RED}{BOLD}❌ Keybox is REVOKED!{RESET}")
else:
    print(f"\n{GREEN}{BOLD}✅ Keybox is STILL VALID!{RESET}")

print(f"\n{CYAN}----------------------------------------{RESET}")
print(f"{CYAN}Check completed successfully.{RESET}\n")
