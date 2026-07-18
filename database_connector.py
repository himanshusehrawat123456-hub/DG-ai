"""
DG AI Version 1
Database Connector

Purpose:
- Handle database connection foundation
- Manage connection status
- Provide database configuration support

Version: 1.0
"""

import logging
from datetime import datetime


class DatabaseConnector:
    """
    Professional Database Connection Manager
    """

    def __init__(self):

        self.connection_status = False

        self.connection_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    def connect(self, database_name):

        record = {
            "database": database_name,
            "status": "connected",
            "time": str(datetime.now())
        }

        self.connection_status = True

        self.connection_history.append(record)

        return record


    def disconnect(self):

        self.connection_status = False

        record = {
            "status": "disconnected",
            "time": str(datetime.now())
        }

        self.connection_history.append(record)

        return record


    def is_connected(self):

        return self.connection_status


    def get_history(self):

        return self.connection_history
