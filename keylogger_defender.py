"""
Keylogger Defender (Advanced Version)
Created by Mira2720 (GitHub: https://github.com/Mira2720) for educational and cybersecurity training purposes.
Adds real-time monitoring, malware signature scanning, desktop alerts, and log export.
"""

import os
import psutil
import time
import csv
import json
import hashlib
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from plyer import notification


import platform

def log_platform_info():
    system = platform.system()
    release = platform.release()
    version = platform.version()
    log_alert(f"Running on platform: {system} {release} (Version: {version})")

# Settings
QUARANTINE_DIR = "quarantine"

def quarantine_file(filepath):
    if not os.path.exists(QUARANTINE_DIR):
        os.makedirs(QUARANTINE_DIR)
    try:
        base_name = os.path.basename(filepath)
        quarantined_path = os.path.join(QUARANTINE_DIR, base_name)
        os.rename(filepath, quarantined_path)
        log_alert(f"Quarantined suspicious file: {filepath}")
    except Exception as e:
        log_alert(f"Failed to quarantine file {filepath}: {e}")

SUSPICIOUS_MODULES = ['pynput', 'keyboard', 'pyperclip']
LOG_DIR = "logs"
LOG_TXT = os.path.join(LOG_DIR, "detection_log.txt")
LOG_JSON = os.path.join(LOG_DIR, "detection_log.json")
LOG_CSV = os.path.join(LOG_DIR, "detection_log.csv")
MALWARE_SIGNATURES = {
    # Simulated example: filename: sha256 hash
    "keylogger.py": "fakehashvalue1234567890abcdef",
}

alerts = []

def notify_user(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Keylogger Defender',
        timeout=5
    )

def log_alert(message):
    timestamp = datetime.now().isoformat()
    alert_entry = {"time": timestamp, "alert": message}
    alerts.append(alert_entry)

    with open(LOG_TXT, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

    notify_user("Keylogger Defender Alert", message)

def detect_suspicious_processes():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            cmdline = ' '.join(proc.info['cmdline']).lower()
            for module in SUSPICIOUS_MODULES:
                if module in cmdline:
                    log_alert(f"Suspicious module '{module}' found in process {proc.info['name']} (PID {proc.info['pid']})")
        except Exception:
            continue

def scan_for_malware_signatures(directory='.'):
    for root, _, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "rb") as f:
                    content = f.read()
                    hash_digest = hashlib.sha256(content).hexdigest()
                    if file in MALWARE_SIGNATURES[file] == hash_digest:
    log_alert(f"Malware signature match for file: {filepath}")
    quarantine_file(filepath)

                        log_alert(f"Malware signature match for file: {filepath}")
            except Exception:
                continue

class LogEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory: return
        if event.src_path.endswith(".txt") or event.src_path.endswith(".log"):
            log_alert(f"Real-time change detected in: {event.src_path}")

def export_logs():
    with open(LOG_JSON, "w") as jf:
        json.dump(alerts, jf, indent=4)

    with open(LOG_CSV, "w", newline='') as cf:
        writer = csv.DictWriter(cf, fieldnames=["time", "alert"])
        writer.writeheader()
        for entry in alerts:
            writer.writerow(entry)

if __name__ == "__main__":
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)

    print("🔎 Starting Keylogger Defender (Advanced)...")
    log_platform_info()

    # Initial passive scans
    detect_suspicious_processes()
    scan_for_malware_signatures()

    # Start real-time monitoring
    event_handler = LogEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(60)  # Run indefinitely, checking every 60 seconds
            export_logs()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    print("🛑 Monitoring stopped. Logs exported.")
