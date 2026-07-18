"""
DG AI Version 1
Knowledge Management System

Purpose:
- Store and manage knowledge
- Search information
- Provide knowledge base foundation

Version: 1.0
"""


import json
import os



class KnowledgeManager:
    """
    Handles DG AI knowledge operations.
    """



    def __init__(self, file_path="data/knowledge.json"):

        self.file_path = file_path

        self.knowledge = {}

        self._create_storage()

        self._load_knowledge()



    def _create_storage(self):
        """
        Create storage folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def add_knowledge(self, topic, information):
        """
        Add new knowledge.
        """

        self.knowledge[topic] = information

        self._save_knowledge()



    def get_knowledge(self, topic):
        """
        Retrieve knowledge.
        """

        return self.knowledge.get(
            topic,
            "Information not found"
        )



    def search_knowledge(self, keyword):
        """
        Search knowledge topics.
        """

        results = []


        for topic in self.knowledge:

            if keyword.lower() in topic.lower():

                results.append(topic)


        return results



    def remove_knowledge(self, topic):
        """
        Remove knowledge.
        """

        if topic in self.knowledge:

            del self.knowledge[topic]

            self._save_knowledge()

            return True


        return False



    def _save_knowledge(self):
        """
        Save knowledge data.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.knowledge,
                file,
                indent=4
            )



    def _load_knowledge(self):
        """
        Load existing knowledge.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.knowledge = json.load(file)




# Testing

if __name__ == "__main__":


    manager = KnowledgeManager()


    manager.add_knowledge(
        "Python",
        "Python is a programming language"
    )


    manager.add_knowledge(
        "DG AI",
        "AI assistant project"
    )


    print(
        manager.get_knowledge(
            "Python"
        )
    )


    print(
        manager.search_knowledge(
            "AI"
        )
    )
