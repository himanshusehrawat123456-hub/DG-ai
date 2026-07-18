"""
DG AI Version 1
Result Manager System

Purpose:
- Manage search results
- Store and retrieve results

Version: 1.0
"""


import datetime



class ResultManager:
    """
    Handles search result management.
    """



    def __init__(self):

        self.results = []



    def add_result(self, query, result):
        """
        Add search result.
        """

        data = {

            "id":
            len(self.results) + 1,

            "query":
            query,

            "result":
            result,

            "time":
            str(datetime.datetime.now())

        }


        self.results.append(data)


        return data



    def get_results(self):
        """
        Return all results.
        """

        return self.results



    def delete_result(self, result_id):
        """
        Delete result by id.
        """

        for item in self.results:

            if item["id"] == result_id:

                self.results.remove(item)

                return True


        return False




# Testing

if __name__ == "__main__":


    manager = ResultManager()


    print(
        manager.add_result(
            "Python",
            "Python is a programming language"
        )
    )
