"""
DG AI Version 1
Memory Search System

Purpose:
- Search stored memories
- Retrieve relevant information

Version: 1.0
"""


import datetime



class MemorySearch:
    """
    Handles memory searching operations.
    """



    def __init__(self):

        self.search_history = []



    def search(self, memories, keyword):
        """
        Search memory using keyword.
        """

        results = []


        for item in memories:

            if isinstance(item, dict):

                text = str(item)

            else:

                text = str(item)



            if keyword.lower() in text.lower():

                results.append(item)



        self.search_history.append({

            "keyword":
            keyword,

            "results":
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


    search_engine = MemorySearch()


    memories = [

        "DG AI Project",

        "Python Learning",

        "Voice Assistant"

    ]


    result = search_engine.search(
        memories,
        "AI"
    )


    print(result)
