from .monitor import Monitor
from .behavioral_engine import BehavioralEngine
from .detector import Detector
from .alerter import Alerter

class RansomwareFramework:
    def __init__(self):
        self.monitor = Monitor()
        self.behavioral_engine = BehavioralEngine()
        self.detector = Detector()
        self.alerter = Alerter()

    def run(self):
        """
        Runs the ransomware profiling framework.
        """
        # Step 1: Monitor and collect data
        data = self.monitor.collect_data()

        # Step 2: Analyze behavior
        anomalies = self.behavioral_engine.analyze_behavior(data)

        # Step 3: Detect ransomware
        if self.detector.detect_ransomware(anomalies):
            # Step 4: Send alert
            self.alerter.send_alert("Ransomware behavior detected!")
        else:
            print("No ransomware behavior detected.")