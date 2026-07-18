"""
DG AI Version 1
Search Manager

Purpose:
- Manage search operations
- Store search results

Version: 1.0
"""

import datetime


class SearchManager:
    """
    Handles search management.
    """

    def __init__(self):
        self.search_records = []

    def add_search(self, query, results_count):

        record = {
            "id": len(self.search_records) + 1,
            "query": query,
            "results": results_count,
            "searched_at": str(datetime.datetime.now())
        }

        self.search_records.append(record)

        return record

    def get_search_records(self):

        return self.search_records

    def clear_search_records(self):

        self.search_records.clear()

        return True


# Testing

if __name__ == "__main__":

    manager = SearchManager()

    print(
        manager.add_search(
            "Python",
            25
        )
    )
