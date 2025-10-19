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

Make sure you have Python 3.8+ installed. The dependencies are listed in `requirements.txt`.

### On standard Linux/macOS

```sh
pip install -r requirements.txt
```

### On Termux

Due to compilation complexities, it is highly recommended to install `cryptography` via `pkg`.

```sh
pkg install python python-cryptography
pip install requests
```
---

## 🚀 Usage

```sh
python3 keybox_check.py /path-to-keybox.xml
```
---

## 🖥️ Example Output

```
🔍 Checking Android Keybox Status...
→ Fetching revocation list from Google...
✔ Revocation list loaded successfully.
→ Parsing XML file: /path/to/your/keybox.xml

Certificate Serial Numbers:
  🔹 EC  Cert SN: b2f9bfdfea06...
  🔹 RSA Cert SN: 37da52dd522c...

❌ Keybox is REVOKED!

----------------------------------------
Check completed successfully.
```

---

## 🙌 Credit
- [hldr4](https://gist.github.com/hldr4/b933f584b2e2c3088bcd56eb056587f8) for original concept and initial version
