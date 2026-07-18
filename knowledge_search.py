"""
DG AI Version 1
Knowledge Search System

Purpose:
- Search stored knowledge
- Find information by topic

Version: 1.0
"""


import datetime



class KnowledgeSearch:
    """
    Handles knowledge search operations.
    """



    def __init__(self):

        self.search_history = []



    def search(self, knowledge_data, keyword):
        """
        Search knowledge by keyword.
        """

        results = []


        for item in knowledge_data:

            if keyword.lower() in item["topic"].lower():

                results.append(item)



        self.search_history.append({

            "keyword":
            keyword,

            "result_count":
            len(results),

            "time":
            str(datetime.datetime.now())

        })


        return results



    def get_search_history(self):
        """
        Return search history.
        """

        return self.search_history



    def clear_history(self):
        """
        Clear search history.
        """

        self.search_history.clear()

        return True




# Testing

if __name__ == "__main__":


    search = KnowledgeSearch()


    data = [

        {
            "topic": "Python",
            "information": "Programming Language"
        },

        {
            "topic": "AI",
            "information": "Artificial Intelligence"
        }

    ]


    print(
        search.search(
            data,
            "Python"
        )
    )
