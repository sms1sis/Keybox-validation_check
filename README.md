# 🔐 Android Keybox Integrity Checker

A simple yet powerful Python script to **check the validity of your Android `keybox.xml` file**, which is crucial for **passing Play Integrity checks** on custom or uncertified Android devices.

This tool verifies whether the **EC and RSA certificates** inside your keybox have been **revoked by Google**, using the official **Android Attestation CRL (Certificate Revocation List)**.

---

## ✨ Features

- 🧩 Parses and extracts certificates from `keybox.xml`
- 🌐 Fetches Google’s live CRL for verification
- 🔎 Displays EC and RSA certificate serial numbers
- ✅ Shows whether your Keybox is **valid or revoked**
- 🎨 Eye-catching, colorized terminal output with clear status indicators
- ⚠️ Graceful error handling for network and XML issues

---

## 📦 Requirements

Make sure you have Python 3.8+ installed, then install the required dependency:

```sh
pip install cryptography requests
```
## On termux use

```sh
pkg install python-cryptography
pip install requests
```
## 🚀 Usage

```sh
python3 keybox_check.py /path-to-keybox.xml
```
## Example output:

```
\033[96m\033[1m🔍 Checking Android Keybox Status...\033[0m
\033[93m→ Fetching revocation list from Google...\033[0m
\033[92m✔ Revocation list loaded successfully.\033[0m
\033[93m→ Parsing XML file: keybox.xml\033[0m

\033[1mCertificate Serial Numbers:\033[0m
  🔹 EC  Cert SN: \033[96m7a8b9c3f2d1e4a...\033[0m
  🔹 RSA Cert SN: \033[96m2d4f8a9c7b1e3...\033[0m

\033[92m\033[1m✅ Keybox is STILL VALID!\033[0m

\033[96m----------------------------------------\033[0m
\033[96mCheck completed successfully.\033[0m
```

## 🙌 Credit
- [hldr4](https://gist.github.com/hldr4/b933f584b2e2c3088bcd56eb056587f8) for original concept and initial version
