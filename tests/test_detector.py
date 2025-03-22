import pytest
from ..core.detector import Detector

def test_detector_detect_threats():
    detector = Detector(threshold=1)
    anomalies = [{"action": "encrypt"}]
    assert detector.detect_threats(anomalies), "Should detect a threat"