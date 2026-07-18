"""
DG AI Version 1
Network Manager

Purpose:
- Manage network operations

Version: 1.0
"""

import datetime


class NetworkManager:

    def __init__(self):
        self.records = []

    def add_record(self, status):

        record = {
            "id": len(self.records) + 1,
            "status": status,
            "time": str(datetime.datetime.now())
        }

        self.records.append(record)

        return record

    def get_records(self):
        return self.records
