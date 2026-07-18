"""
DG AI Version 1
Monitoring Manager

Purpose:
- Manage system monitoring
- Store monitoring records

Version: 1.0
"""

import datetime


class MonitoringManager:
    """
    Handles monitoring operations.
    """

    def __init__(self):
        self.records = []

    def add_record(self, module_name, status):
        """
        Add monitoring record.
        """

        record = {
            "id": len(self.records) + 1,
            "module": module_name,
            "status": status,
            "time": str(datetime.datetime.now())
        }

        self.records.append(record)

        return record

    def get_records(self):
        """
        Return all monitoring records.
        """

        return self.records

    def clear_records(self):
        """
        Clear monitoring records.
        """

        self.records.clear()

        return True


# Testing

if __name__ == "__main__":

    monitor = MonitoringManager()

    print(
        monitor.add_record(
            "Voice System",
            "Running"
        )
    )
