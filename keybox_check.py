import requests
import sys
import xml.etree.ElementTree as ET
import argparse
from cryptography import x509

# ANSI color codes for pretty output
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def parse_cert(cert_pem):
    """Parses a PEM certificate string and returns its serial number as a hex string."""
    cert_pem = "\n".join(line.strip() for line in cert_pem.strip().split("\n"))
    cert = x509.load_pem_x509_certificate(cert_pem.encode())
    return f"{cert.serial_number:x}"

def main():
    """Main function to run the keybox check."""
    parser = argparse.ArgumentParser(
        description="Check the validity of an Android keybox.xml file against Google's CRL.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("xml_file", help="Path to the keybox.xml file.")
    args = parser.parse_args()

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
        print(f"{YELLOW}→ Parsing XML file: {args.xml_file}{RESET}")
        certs = [elem.text for elem in ET.parse(args.xml_file).getroot().iter() if elem.text and "BEGIN CERTIFICATE" in elem.text]
        if len(certs) < 4:
            raise ValueError("XML does not contain enough certificates.")
    except Exception as e:
        print(f"{RED}✖ Failed to parse XML: {e}{RESET}")
        sys.exit(1)

    # Extract EC and RSA serial numbers
    try:
        ec_cert_sn = parse_cert(certs[0])
        rsa_cert_sn = parse_cert(certs[3])
    except Exception as e:
        print(f"{RED}✖ Failed to parse certificates: {e}{RESET}")
        sys.exit(1)

    print(f"\n{BOLD}Certificate Serial Numbers:{RESET}")
    print(f"  🔹 EC  Cert SN: {CYAN}{ec_cert_sn}{RESET}")
    print(f"  🔹 RSA Cert SN: {CYAN}{rsa_cert_sn}{RESET}")

    # Check revocation
    revoked_serials = crl.get("entries", {})
    is_ec_revoked = ec_cert_sn in revoked_serials
    is_rsa_revoked = rsa_cert_sn in revoked_serials

    if is_ec_revoked or is_rsa_revoked:
        print(f"\n{RED}{BOLD}❌ Keybox is REVOKED!{RESET}")

    else:
        print(f"\n{GREEN}{BOLD}✅ Keybox is STILL VALID!{RESET}")

    print(f"\n{CYAN}----------------------------------------{RESET}")
    print(f"{CYAN}Check completed successfully.{RESET}\n")

if __name__ == "__main__":
    main()