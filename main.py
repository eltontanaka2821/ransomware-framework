from src.rbprof.core.monitor import MonitoringModule
from src.rbprof.core.alerter import AlertingModule
from src.rbprof.core.detector import DetectionModule
from src.rbprof.core.behavioral_engine import BehaviorEngine


if __name__ == "__main__":
    # Initialize components
    monitor = MonitoringModule()
    behavior = BehaviorEngine()
    detector = DetectionModule()
    alerter = AlertingModule()

    # Example file input
    input_file = "malware.exe"  # Try "normal.docx" for comparison
    
    # Step 1: X → X'
    x_prime = monitor.scan(input_file)
    print(f"Monitoring Output (X'):\n{json.dumps(x_prime, indent=2)}")
    
    # Step 2: X' → X''
    x_double_prime = behavior.analyze(x_prime)
    print(f"\nBehavioral Analysis (X''):\n{json.dumps(x_double_prime, indent=2)}")
    
    # Step 3: X'' → Scored
    x_scored = detector.evaluate(x_double_prime)
    print(f"\nThreat Scoring:\n{json.dumps(x_scored, indent=2)}")
    
    # Step 4: Final Verdict
    final_report = alerter.decide(x_scored)
    print(f"\nFinal Report:\n{json.dumps(final_report, indent=2)}")