# 🛡️ Keylogger Defender (Advanced)
<<<<<<< HEAD
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Repo size](https://img.shields.io/github/repo-size/Mira2720/keylogger-defender-advanced)


=======
>>>>>>> 9f37feb26e97a53f32afe682b72c2fc21b0f2dce

**Created by Mira2720 (GitHub: https://github.com/Mira2720)**

This advanced version of the original Keylogger Defender now includes real-time monitoring, malware signature detection, desktop notifications, and log exports to JSON/CSV.

## 🚀 Features

- ✅ Real-time file system monitoring using `watchdog`
- ✅ Desktop notifications for live alerts (`plyer`)
- ✅ Malware signature matching by SHA256 hash
- ✅ Log export to `.json` and `.csv`
- ✅ Monitors use of known keylogger libraries (`pynput`, `keyboard`, `pyperclip`)

## 🔧 Setup

1. Clone or download the repo
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run it:

```bash
python keylogger_defender.py
```

## 📦 Output

- Alerts shown in real-time via desktop notification
- Logs written to:
  - `logs/detection_log.txt`
  - `logs/detection_log.json`
  - `logs/detection_log.csv`

## 📚 Future Ideas

- Build a GUI dashboard
- Integrate with a basic local SIEM system
- Include external YARA rule support
- Quarantine suspicious files

---

<<<<<<< HEAD
⚠️ **Educational use only. Unauthorized monitoring or scanning without consent is illegal.**
=======
⚠️ **Educational use only. Unauthorized monitoring or scanning without consent is illegal.**
>>>>>>> 9f37feb26e97a53f32afe682b72c2fc21b0f2dce
