# 📘 Attribution
**Created by Mira2720 (GitHub: https://github.com/Mira2720)**

# 🧪 Case Study: How Keylogger Defender Caught a Keylogger

## 🧠 Scenario

As part of my cybersecurity learning journey, I created two related tools:

- **🔐 Keylogger (Educational)** – Simulates a red team-style keylogger that captures keystrokes, clipboard data, and sends periodic emails.
- **🛡️ Keylogger Defender** – A blue team tool that detects keylogger behaviors in real-time and alerts/logs the results.

This case study demonstrates how the **defender** successfully detected and flagged the offensive tool.

---

## 🖥️ Setup

- Ran `keylogger.py` in a simulated lab environment (macOS)
- Launched `keylogger_defender.py` simultaneously
- Defender was configured to:
  - Monitor system processes
  - Watch for file system changes
  - Look for common keylogger libraries (`pynput`, `keyboard`, `pyperclip`)
  - Check for known malicious file hashes
  - Send desktop alerts and export logs

---

## 🔍 What Happened During the Test

| Timeline | Event |
|---------|-------|
| `00:00` | Keylogger script started in terminal |
| `00:01` | Defender detected use of `pynput` in running process |
| `00:01` | Alert popped up: “⚠️ Suspicious module 'pynput' found in process python3” |
| `00:02` | Defender noticed rapid updates to `keystrokes.txt` log file |
| `00:03` | Alert triggered: “⚠️ Real-time change detected in logs/keystrokes.txt” |
| `00:05` | Defender scanned `keylogger.py`, found hash match, and quarantined the file |
| `00:05` | Logs exported to `.txt`, `.csv`, and `.json` formats for analysis |

---

## 📦 Detection Log (Sample)

```
[2025-04-09T21:13:15] Suspicious module 'pynput' found in process python3 (PID 4932)
[2025-04-09T21:13:30] Real-time change detected in: logs/keystrokes.txt
[2025-04-09T21:14:02] Malware signature match for file: keylogger.py
[2025-04-09T21:14:02] Quarantined suspicious file: keylogger.py
```

---

## 🧾 Exported Reports

- `detection_log.txt` – Plain-text summary
- `detection_log.json` – Used for structured reporting
- `detection_log.csv` – Opened in Excel for log review

---

## ✅ What This Proves

- The defender script **successfully identified the offensive behavior** in multiple ways.
- It demonstrated knowledge of both **red team techniques** and **blue team response strategies**.
- The combination of tools simulates a real-world attack-defense scenario.
- Shows how simple behavioral detection can stop stealthy scripts in a lab setting.

---

## 🛠️ Next Steps

- Add YARA rule support for deeper static analysis
- Build a web-based dashboard using Flask or Streamlit
- Expand the malware signature DB to cover more cases
- Trigger remote alerts (email, webhook)

---
