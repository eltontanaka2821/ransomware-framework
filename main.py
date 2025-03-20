import os
import re
from datetime import datetime

# Predefined rules for ransomware behavior
RANSOMWARE_PATTERNS = {
    "encryption": re.compile(r"encrypt|aes|rsa|des", re.IGNORECASE),
    "suspicious_process": re.compile(r"ransom|malware|trojan", re.IGNORECASE),
    "file_modification": re.compile(r"\.encrypted|\.locked|\.ransom", re.IGNORECASE),
    "suspicious_root": re.compile(r"/root|/admin", re.IGNORECASE),
}

# Security levels based on confidence score
SECURITY_LEVELS = {
    0: "Low",
    1: "Medium",
    2: "High",
    3: "Critical"
}

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

def display_results(results):
    """
    Display the results in the specified format.
    """
    print("filename----status----root------process_name-----description---confidence_score------security_level")
    for result in results:
        print(
            f"{result['filename']}----{result['status']}----{result['root']}------"
            f"{result['process_name']}-----{result['description']}---{result['confidence_score']}------"
            f"{result['security_level']}"
        )

# Example log entries
logs = [
    {"filename": "document.txt.encrypted", "path": "/home/user/documents", "process_name": "ransomware.exe", "description": "File encrypted using AES-256."},
    {"filename": "photo.jpg", "path": "/home/user/pictures", "process_name": "image_viewer.exe", "description": "File opened for viewing."},
    {"filename": "report.pdf", "path": "/root/documents", "process_name": "malware.exe", "description": "File accessed by suspicious process."},
    {"filename": "data.db", "path": "/home/user/database", "process_name": "backup_tool.exe", "description": "File backed up successfully."},
]

# Process logs and display results
results = process_logs(logs)
display_results(results)