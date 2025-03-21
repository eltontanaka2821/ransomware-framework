import logging
import time
from collections import defaultdict
from typing import Dict, List

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock data source (e.g., logs, network traffic)
class DataSource:
    def __init__(self):
        self.data = [
            {"timestamp": time.time(), "user": "admin", "action": "login", "source_ip": "192.168.1.1"},
            {"timestamp": time.time(), "user": "user1", "action": "access_file", "file": "secret.txt"},
            {"timestamp": time.time(), "user": "admin", "action": "logout", "source_ip": "192.168.1.1"},
            {"timestamp": time.time(), "user": "attacker", "action": "brute_force", "source_ip": "10.0.0.1"},
        ]

    def get_data(self):
        return self.data

# Monitoring Component
class Monitor:
    def __init__(self, data_source):
        self.data_source = data_source

    def collect_data(self):
        return self.data_source.get_data()

# Behavioral Engine Component
class BehavioralEngine:
    def __init__(self):
        self.normal_behavior = {"admin": ["login", "logout"], "user1": ["access_file"]}

    def analyze_behavior(self, data: List[Dict]):
        anomalies = []
        for entry in data:
            user = entry.get("user")
            action = entry.get("action")
            if user in self.normal_behavior:
                if action not in self.normal_behavior[user]:
                    anomalies.append(entry)
            else:
                anomalies.append(entry)
        return anomalies

# Detection Component
class Detector:
    def __init__(self):
        self.threat_rules = [
            {"action": "brute_force", "description": "Potential brute force attack"},
            {"action": "access_file", "file": "secret.txt", "description": "Unauthorized access to secret file"}
        ]

    def detect_threats(self, data: List[Dict]):
        detected_threats = []
        for entry in data:
            for rule in self.threat_rules:
                if all(entry.get(key) == value for key, value in rule.items() if key != "description"):
                    detected_threats.append((entry, rule["description"]))
        return detected_threats

# Alerting Component
class Alerter:
    def __init__(self):
        pass

    def send_alert(self, message):
        logging.warning(f"ALERT: {message}")

# Main Framework
class CybersecurityFramework:
    def __init__(self):
        self.data_source = DataSource()
        self.monitor = Monitor(self.data_source)
        self.behavioral_engine = BehavioralEngine()
        self.detector = Detector()
        self.alerter = Alerter()

    def run(self):
        # Step 1: Monitor and collect data
        data = self.monitor.collect_data()
        logging.info("Data collected for analysis.")

        # Step 2: Analyze behavior
        anomalies = self.behavioral_engine.analyze_behavior(data)
        if anomalies:
            logging.info(f"Behavioral anomalies detected: {anomalies}")

        # Step 3: Detect threats
        threats = self.detector.detect_threats(data)
        if threats:
            for threat, description in threats:
                logging.info(f"Threat detected: {threat} - {description}")
                # Step 4: Send alerts
                self.alerter.send_alert(f"Threat detected: {description}")

# Run the framework
if __name__ == "__main__":
    framework = CybersecurityFramework()
    framework.run()