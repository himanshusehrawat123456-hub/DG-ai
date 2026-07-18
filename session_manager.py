"""
DG AI Version 1
Session Management System

Purpose:
- Manage user sessions
- Track active sessions
- Provide authentication foundation

Version: 1.0
"""


import datetime
import uuid



class SessionManager:
    """
    Handles DG AI user sessions.
    """



    def __init__(self):

        self.sessions = []



    def create_session(self, user_id):
        """
        Create new user session.
        """

        session = {

            "session_id":
            str(uuid.uuid4()),

            "user_id":
            user_id,

            "status":
            "Active",

            "created":
            str(datetime.datetime.now())

        }


        self.sessions.append(session)


        return session



    def get_session(self, session_id):
        """
        Find session by ID.
        """

        for session in self.sessions:

            if session["session_id"] == session_id:

                return session


        return None



    def close_session(self, session_id):
        """
        Close active session.
        """

        for session in self.sessions:

            if session["session_id"] == session_id:

                session["status"] = "Closed"

                return True


        return False



    def get_active_sessions(self):
        """
        Return active sessions.
        """

        return [

            session

            for session in self.sessions

            if session["status"] == "Active"

        ]




# Testing

if __name__ == "__main__":


    manager = SessionManager()


    session = manager.create_session(
        "User_001"
    )


    print(
        "New Session:"
    )

    print(session)


    print(
        "\nActive Sessions:"
    )

    print(
        manager.get_active_sessions()
    )
