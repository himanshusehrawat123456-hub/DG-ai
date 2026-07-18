"""
DG AI Version 1
Knowledge Update System

Purpose:
- Update existing knowledge
- Manage knowledge changes

Version: 1.0
"""


import datetime



class KnowledgeUpdate:
    """
    Handles knowledge update operations.
    """



    def __init__(self):

        self.update_history = []



    def update_knowledge(self, knowledge_data, knowledge_id, new_information):
        """
        Update knowledge record.
        """

        for item in knowledge_data:

            if item["id"] == knowledge_id:

                old_information = item["information"]

                item["information"] = new_information


                self.update_history.append({

                    "id":
                    knowledge_id,

                    "old":
                    old_information,

                    "new":
                    new_information,

                    "time":
                    str(datetime.datetime.now())

                })


                return True


        return False



    def get_update_history(self):
        """
        Return update history.
        """

        return self.update_history



    def clear_history(self):
        """
        Clear update history.
        """

        self.update_history.clear()

        return True




# Testing

if __name__ == "__main__":


    updater = KnowledgeUpdate()


    data = [

        {
            "id": 1,
            "topic": "Python",
            "information": "Basic Language"
        }

    ]


    updater.update_knowledge(
        data,
        1,
        "Advanced Programming Language"
    )


    print(data)
