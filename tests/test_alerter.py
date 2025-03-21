import logging
from framework.core.alerter import Alerter

def test_alerter_send_alert(caplog):
    alerter = Alerter()
    alerter.send_alert("Test alert")
    assert "ALERT: Test alert" in caplog.text, "Alert message should be logged"