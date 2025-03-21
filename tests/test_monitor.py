import pytest
from framework.core.monitor import Monitor

def test_monitor_collect_data():
    monitor = Monitor()
    data = monitor.collect_data()
    assert isinstance(data, list), "Data should be a list"
    assert len(data) > 0, "Data should not be empty"