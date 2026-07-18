"""
DG AI Version 1
Knowledge Store System

Purpose:
- Store AI knowledge data
- Manage knowledge records

Version: 1.0
"""


import datetime



class KnowledgeStore:
    """
    Handles knowledge storage operations.
    """



    def __init__(self):

        self.knowledge = []



    def add_knowledge(self, topic, information):
        """
        Store new knowledge.
        """

        record = {

            "id":
            len(self.knowledge) + 1,

            "topic":
            topic,

            "information":
            information,

            "time":
            str(datetime.datetime.now())

        }


        self.knowledge.append(record)


        return record



    def get_all_knowledge(self):
        """
        Return all knowledge
