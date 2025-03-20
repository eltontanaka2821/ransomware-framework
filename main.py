import os
import re
import time
import threading
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined rules for ransomware behavior
RANSOMWARE_PATTERNS = {
    "encryption": re.compile(r"encrypt|aes|rsa|des", re.IGNORECASE),
    "suspicious_process": re.compile(r"ransom|malware|trojan", re.IGNORECASE),
    "file_modification": re.compile(r"\.encrypted|\.locked|\.ransom", re.IGNORECASE),
    "suspicious_root": re.compile(r"/root|/admin", re.IGNORECASE),
    "suspicious_network": re.compile(r"tor|vpn|proxy", re.IGNORECASE),
    "suspicious_cloud": re.compile(r"unauthorized|access denied", re.IGNORECASE),
}

# Security levels based on confidence score
SECURITY_LEVELS = {
    0: "Low",
    1: "Medium",
    2: "High",
    3: "Critical"
}

# Simulated log storage
logs = []

def analyze_log(log_entry):
    """
    Analyze a log entry for ransomware behavior.
    """
    filename = log_entry.get("filename", "unknown")
    status = "Clean"
    root = "No"
    process_name = log_entry.get("process_name", "unknown")
    description = ""
    confidence_score = 0

    # Check for suspicious root access
    if RANSOMWARE_PATTERNS["suspicious_root"].search(log_entry.get("path", "")):
        root = "Yes"
        confidence_score += 1
        description += "Suspicious root access detected. "

    # Check for suspicious process names
    if RANSOMWARE_PATTERNS["suspicious_process"].search(process_name):
        confidence_score += 1
        description += "Suspicious process name detected. "

    # Check for file modifications indicating encryption
    if RANSOMWARE_PATTERNS["file_modification"].search(filename):
        confidence_score += 2
        description += "File modification indicating encryption detected. "
        status = "Suspicious"

    # Check for encryption-related keywords in the log
    if RANSOMWARE_PATTERNS["encryption"].search(log_entry.get("description", "")):
        confidence_score += 1
        description += "Encryption-related activity detected. "
        status = "Suspicious"

    # Check for suspicious network activity
    if RANSOMWARE_PATTERNS["suspicious_network"].search(log_entry.get("network_log", "")):
        confidence_score += 1
        description += "Suspicious network activity detected. "
        status = "Suspicious"

    # Check for suspicious cloud activity
    if RANSOMWARE_PATTERNS["suspicious_cloud"].search(log_entry.get("cloud_log", "")):
        confidence_score += 1
        description += "Suspicious cloud activity detected. "
        status = "Suspicious"

    # Determine security level based on confidence score
    security_level = SECURITY_LEVELS.get(min(confidence_score, 3), "Unknown")

    return {
        "filename": filename,
        "status": status,
        "root": root,
        "process_name": process_name,
        "description": description.strip(),
        "confidence_score": confidence_score,
        "security_level": security_level
    }

def process_logs(logs):
    """
    Process a list of log entries and generate results.
    """
    results = []
    for log in logs:
        result = analyze_log(log)
        results.append(result)
    return results

def monitor_network():
    """
    Simulate network monitoring.
    """
    while True:
        # Simulate network log generation
        network_log = {
            "filename": "network_log",
            "path": "/var/log/network",
            "process_name": "network_service",
            "description": "Network activity detected.",
            "network_log": "tor connection established"
        }
        logs.append(network_log)
        time.sleep(10)

def monitor_cloud():
    """
    Simulate cloud access monitoring.
    """
    while True:
        # Simulate cloud log generation
        cloud_log = {
            "filename": "cloud_log",
            "path": "/var/log/cloud",
            "process_name": "cloud_service",
            "description": "Cloud access detected.",
            "cloud_log": "unauthorized access attempt"
        }
        logs.append(cloud_log)
        time.sleep(15)

@app.route("/")
def index():
    """
    Render the front-end interface.
    """
    return render_template("index.html")

@app.route("/get_logs", methods=["GET"])
def get_logs():
    """
    Return processed logs to the front-end.
    """
    results = process_logs(logs)
    return jsonify(results)

@app.route("/add_log", methods=["POST"])
def add_log():
    """
    Allow users to add custom logs.
    """
    log_entry = request.json
    logs.append(log_entry)
    return jsonify({"status": "Log added successfully"})

if __name__ == "__main__":
    # Start network and cloud monitoring in separate threads
    threading.Thread(target=monitor_network, daemon=True).start()
    threading.Thread(target=monitor_cloud, daemon=True).start()

    # Start the Flask app
    app.run(debug=True)