"""
DG AI Version 1
Database Management System

Purpose:
- Manage DG AI data storage
- Provide database foundation
- Handle save and retrieve operations

Version: 1.0
"""


import sqlite3
import os



class DatabaseManager:
    """
    Handles DG AI database operations.
    """



    def __init__(self, database="data/dg_ai.db"):

        self.database = database

        self._create_folder()

        self.connection = sqlite3.connect(
            self.database
        )

        self.cursor = (
            self.connection.cursor()
        )

        self.create_tables()



    def _create_folder(self):
        """
        Create database folder.
        """

        folder = os.path.dirname(
            self.database
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def create_tables(self):
        """
        Create required database tables.
        """

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memory
            (
                id INTEGER PRIMARY KEY,
                key TEXT UNIQUE,
                value TEXT
            )
            """
        )


        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS logs
            (
                id INTEGER PRIMARY KEY,
                message TEXT
            )
            """
        )


        self.connection.commit()



    def save_memory(self, key, value):
        """
        Store data in memory table.
        """

        self.cursor.execute(
            """
            INSERT OR REPLACE INTO memory
            (key,value)
            VALUES (?,?)
            """,
            (key, value)
        )


        self.connection.commit()



    def get_memory(self, key):
        """
        Retrieve stored memory.
        """

        self.cursor.execute(
            """
            SELECT value FROM memory
            WHERE key=?
            """,
            (key,)
        )


        result = self.cursor.fetchone()


        if result:

            return result[0]


        return None



    def add_log(self, message):
        """
        Save system log.
        """

        self.cursor.execute(
            """
            INSERT INTO logs(message)
            VALUES(?)
            """,
            (message,)
        )


        self.connection.commit()



    def close(self):
        """
        Close database connection.
        """

        self.connection.close()




# Testing

if __name__ == "__main__":


    db = DatabaseManager()


    db.save_memory(
        "AI_Name",
        "DG AI"
    )


    print(
        "Memory:",
        db.get_memory("AI_Name")
    )


    db.add_log(
        "Database System Tested"
    )


    db.close()


    print(
        "Database Ready"
    )
