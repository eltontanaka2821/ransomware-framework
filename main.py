from src.rbprof.core.monitor import MonitoringModule
from src.rbprof.core.alerter import AlertingModule
from src.rbprof.core.detector import DetectionModule
from src.rbprof.core.behavioral_engine import BehaviorEngine

import json

class SafeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer, np.floating)):
            return int(obj) if isinstance(obj, np.integer) else float(obj)
        elif isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)


if __name__ == "__main__":
    monitor = MonitoringModule()
    
    # Test with both normal and suspicious files
    for file in ["Id.jpg", "Motivation.docx"]:
        try:
            x_prime = monitor.scan(file)
            print(f"Scan results for {file}:")
            print(json.dumps(x_prime, indent=2, cls=SafeEncoder))
        except Exception as e:
            print(f"Error scanning {file}: {str(e)}")