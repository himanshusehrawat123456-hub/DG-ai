"""
DG AI Version 1
Search History System

Purpose:
- Store search history
- Manage previous searches

Version: 1.0
"""


import datetime



class SearchHistory:
    """
    Handles search history operations.
    """



    def __init__(self):

        self.history = []



    def add_history(self, query):
        """
        Add search history record.
        """

        record = {

            "id":
            len(self.history) + 1,

            "query":
            query,

            "time":
            str(datetime.datetime.now())

        }


        self.history.append(record)


        return record



    def get_history(self):
        """
        Return all search history.
        """

        return self.history



    def remove_history(self, history_id):
        """
        Remove history record.
        """

        for item in self.history:

            if item["id"] == history_id:

                self.history.remove(item)

                return True


        return False



    def clear_history(self):
        """
        Clear all history.
        """

        self.history.clear()

        return True




# Testing

if __name__ == "__main__":


    history = SearchHistory()


    history.add_history(
        "DG AI features"
    )


    print(
        history.get_history()
    )
