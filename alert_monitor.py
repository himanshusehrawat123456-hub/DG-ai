"""
DG AI Version 1
Alert Monitor

Purpose:
- Create system alerts
- Track warnings and errors
- Manage alert history

Version: 1.0
"""

import logging
from datetime import datetime


class AlertMonitor:
    """
    Professional Alert Monitoring System
    """

    def __init__(self):

        self.alerts = []

        self.alert_rules = {}

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def add_rule(
        self,
        name,
        condition
    ):
        """
        Add alert rule.
        """

        self.alert_rules[name] = condition


        return True


    # ---------------------------------

    def create_alert(
        self,
        alert_type,
        message,
        level="warning"
    ):
        """
        Create new alert.
        """

        alert = {

            "id":
            len(self.alerts) + 1,

            "type":
            alert_type,

            "message":
            message,

            "level":
            level,

            "status":
            "active",

            "time":
            str(datetime.now())

        }


        self.alerts.append(
            alert
        )


        return alert


    # ---------------------------------

    def resolve_alert(
        self,
        alert_id
    ):
        """
        Mark alert as resolved.
        """

        for alert in self.alerts:

            if alert["id"] == alert_id:

                alert["status"] = "resolved"

                return True


        return False


    # ---------------------------------

    def get_active_alerts(self):
        """
        Return active alerts.
        """

        return [

            alert for alert in self.alerts

            if alert["status"] == "active"

        ]


    # ---------------------------------

    def get_alerts_by_level(
        self,
        level
    ):
        """
        Filter alerts by level.
        """

        return [

            alert for alert in self.alerts

            if alert["level"] == level

        ]


    # ---------------------------------

    def get_all_alerts(self):

        return self.alerts


    # ---------------------------------

    def clear_alerts(self):

        self.alerts.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    monitor = AlertMonitor()


    print(
        monitor.create_alert(
            "system",
            "High memory usage",
            "critical"
        )
    )
