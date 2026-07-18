"""
DG AI Version 1
Error Tracker System

Purpose:
- Track system errors
- Maintain error history

Version: 1.0
"""


import datetime



class ErrorTracker:
    """
    Handles error tracking operations.
    """



    def __init__(self):

        self.errors = []



    def add_error(self, module, error):
        """
        Add error record.
        """

        data = {

            "id":
            len(self.errors) + 1,

            "module":
            module,

            "error":
            error,

            "time":
            str(datetime.datetime.now())

        }


        self.errors.append(data)


        return True



    def get_errors(self):
        """
        Return all errors.
        """

        return self.errors



    def clear_errors(self):
        """
        Clear error history.
        """

        self.errors.clear()

        return True




# Testing

if __name__ == "__main__":


    tracker = ErrorTracker()


    tracker.add_error(
        "AI Core",
        "Test error"
    )


    print(
        tracker.get_errors()
    )
