from cybersecurity_framework.core.monitor import Monitor
from cybersecurity_framework.core.behavioral_engine import BehavioralEngine
from cybersecurity_framework.core.detector import Detector
from cybersecurity_framework.core.alerter import Alerter

def main():
    # Initialize components
    monitor = Monitor()
    behavioral_engine = BehavioralEngine()
    detector = Detector()
    alerter = Alerter()

    # Run the framework
    data = monitor.collect_data()
    anomalies = behavioral_engine.analyze_behavior(data)
    if detector.detect_threats(anomalies):
        alerter.send_alert("Ransomware behavior detected!")
    else:
        print("No threats detected.")

if __name__ == "__main__":
    main()