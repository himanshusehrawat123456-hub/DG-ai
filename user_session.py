"""
DG AI Version 1
User Session System

Purpose:
- Manage user sessions
- Track active users

Version: 1.0
"""


import datetime



class UserSession:
    """
    Handles user sessions.
    """



    def __init__(self):

        self.sessions = []



    def create_session(self, user_id):
        """
        Create user session.
        """

        session = {

            "id":
            len(self.sessions) + 1,

            "user_id":
            user_id,

            "status":
            "Active",

            "login_time":
            str(datetime.datetime.now())

        }


        self.sessions.append(session)


        return session



    def end_session(self, user_id):
        """
        End user session.
        """

        for session in self.sessions:

            if session["user_id"] == user_id:

                session["status"] = "Closed"

                return True


        return False



    def get_sessions(self):
        """
        Return sessions.
        """

        return self.sessions




# Testing

if __name__ == "__main__":


    session = UserSession()


    print(
        session.create_session(
            "user1"
        )
    )
