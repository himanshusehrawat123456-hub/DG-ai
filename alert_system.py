"""
DG AI Version 1
Alert System

Purpose:
- Manage system alerts
- Store alert records

Version: 1.0
"""


import datetime



class AlertSystem:
    """
    Handles alert operations.
    """



    def __init__(self):

        self.alerts = []



    def create_alert(self, alert_type, message):
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

            "status":
            "Active",

            "time":
            str(datetime.datetime.now())

        }


        self.alerts.append(alert)


        return alert



    def close_alert(self, alert_id):
        """
        Close existing alert.
        """

        for alert in self.alerts:

            if alert["id"] == alert_id:

                alert["status"] = "Closed"

                return True


        return False



    def get_alerts(self):
        """
        Return all alerts.
        """

        return self.alerts




# Testing

if __name__ == "__main__":


    system = AlertSystem()


    print(
        system.create_alert(
            "Warning",
            "System update required"
        )
    )
