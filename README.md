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

```bash
pip install cryptography requests

# On termux

```bash
pkg install python-cryptography
pip install requests
