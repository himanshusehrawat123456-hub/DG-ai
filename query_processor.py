"""
DG AI Version 1
Query Processor System

Purpose:
- Process user search queries
- Clean and prepare queries

Version: 1.0
"""


import datetime



class QueryProcessor:
    """
    Handles query processing.
    """



    def __init__(self):

        self.processed_queries = []



    def process_query(self, query):
        """
        Clean and process query.
        """

        processed = {

            "id":
            len(self.processed_queries) + 1,

            "original":
            query,

            "processed":
            query.strip().lower(),

            "time":
            str(datetime.datetime.now())

        }


        self.processed_queries.append(processed)


        return processed



    def get_queries(self):
        """
        Return processed queries.
        """

        return self.processed_queries



    def clear_queries(self):
        """
        Clear query history.
        """

        self.processed_queries.clear()

        return True




# Testing

if __name__ == "__main__":


    processor = QueryProcessor()


    print(
        processor.process_query(
            "  Python AI  "
        )
    )
