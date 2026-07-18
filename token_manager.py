"""
DG AI Version 1
Token Management System

Purpose:
- Manage text tokens
- Provide token processing foundation

Version: 1.0
"""


import datetime



class TokenManager:
    """
    Handles DG AI token operations.
    """



    def __init__(self):

        self.token_history = []



    def tokenize(self, text):
        """
        Convert text into tokens.
        """

        tokens = text.split()


        record = {

            "text":
            text,

            "tokens":
            tokens,

            "count":
            len(tokens),

            "time":
            str(datetime.datetime.now())

        }


        self.token_history.append(record)


        return tokens



    def count_tokens(self, text):
        """
        Count total tokens.
        """

        return len(
            text.split()
        )



    def get_history(self):
        """
        Return token history.
        """

        return self.token_history



    def clear_history(self):
        """
        Clear token history.
        """

        self.token_history.clear()

        return True




# Testing

if __name__ == "__main__":


    manager = TokenManager()


    result = manager.tokenize(
        "Hello DG AI how are you"
    )


    print(result)


    print(
        manager.count_tokens(
            "Hello DG AI"
        )
    )
