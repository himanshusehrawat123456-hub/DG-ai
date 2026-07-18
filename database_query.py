"""
DG AI Version 1
Database Query

Purpose:
- Search database records
- Filter data
- Manage query operations

Version: 1.0
"""


class DatabaseQuery:


    def __init__(self):

        self.query_history = []


    def search(
        self,
        data,
        keyword
    ):

        results = []


        for item in data:

            if keyword.lower() in str(item).lower():

                results.append(item)


        self.query_history.append({

            "keyword": keyword,

            "results": len(results)

        })


        return results



    def filter_data(
        self,
        data,
        key,
        value
    ):

        results = []


        for item in data:

            if item.get(key) == value:

                results.append(item)


        return results



    def get_history(self):

        return self.query_history
