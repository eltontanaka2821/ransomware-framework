import pytest
from framework.core.behavioral_engine import BehavioralEngine

def test_behavioral_engine_analyze_behavior():
    engine = BehavioralEngine()
    data = [{"action": "encrypt"}, {"action": "open"}]
    anomalies = engine.analyze_behavior(data)
    assert len(anomalies) == 1, "Should detect one anomaly"