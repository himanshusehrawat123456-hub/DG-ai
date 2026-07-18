"""
DG AI Version 1
Knowledge Base System

Purpose:
- Store and retrieve knowledge data
- Learning foundation

Version: 1.0
"""


import datetime



class KnowledgeBase:
    """
    Handles knowledge storage.
    """



    def __init__(self):

        self.knowledge = []



    def add_knowledge(self, topic, information):
        """
        Add new knowledge.
        """

        data = {

            "id":
            len(self.knowledge) + 1,

            "topic":
            topic,

            "information":
            information,

            "time":
            str(datetime.datetime.now())

        }


        self.knowledge.append(data)


        return True



    def search_knowledge(self, topic):
        """
        Search knowledge by topic.
        """

        results = []


        for item in self.knowledge:

            if item["topic"].lower() == topic.lower():

                results.append(item)


        return results



    def get_all_knowledge(self):
        """
        Return all knowledge.
        """

        return self.knowledge




# Testing

if __name__ == "__main__":


    kb = KnowledgeBase()


    kb.add_knowledge(
        "Python",
        "Programming language"
    )


    print(
        kb.get_all_knowledge()
    )
