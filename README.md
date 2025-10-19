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
---

## 🖥️ Example Output

```
**🔍 Checking Android Keybox Status...**
➡️ Fetching revocation list from Google...
✔️ Revocation list loaded successfully.
➡️ Parsing XML file: keybox.xml

**Certificate Serial Numbers:**
  🔹 EC  Cert SN: `7a8b9c3f2d1e4a...`
  🔹 RSA Cert SN: `2d4f8a9c7b1e3...`

✅ **Keybox is STILL VALID!**

----------------------------------------
Check completed successfully.
```

---

## 🙌 Credit
- [hldr4](https://gist.github.com/hldr4/b933f584b2e2c3088bcd56eb056587f8) for original concept and initial version
