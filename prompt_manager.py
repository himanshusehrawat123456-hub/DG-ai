"""
DG AI Version 1
Prompt Management System

Purpose:
- Manage AI prompts
- Store and retrieve instructions

Version: 1.0
"""


import datetime



class PromptManager:
    """
    Handles DG AI prompt operations.
    """



    def __init__(self):

        self.prompts = []



    def add_prompt(self, name, prompt):
        """
        Add new prompt.
        """

        data = {

            "id":
            len(self.prompts) + 1,

            "name":
            name,

            "prompt":
            prompt,

            "time":
            str(datetime.datetime.now())

        }


        self.prompts.append(data)


        return True



    def get_prompt(self, name):
        """
        Get prompt by name.
        """

        for item in self.prompts:

            if item["name"] == name:

                return item


        return None



    def get_all_prompts(self):
        """
        Return all prompts.
        """

        return self.prompts



    def update_prompt(self, name, new_prompt):
        """
        Update existing prompt.
        """

        for item in self.prompts:

            if item["name"] == name:

                item["prompt"] = new_prompt

                item["updated_time"] = (
                    str(datetime.datetime.now())
                )

                return True


        return False



    def delete_prompt(self, name):
        """
        Delete prompt.
        """

        for item in self.prompts:

            if item["name"] == name:

                self.prompts.remove(item)

                return True


        return False




# Testing

if __name__ == "__main__":


    manager = PromptManager()


    manager.add_prompt(
        "Assistant",
        "You are DG AI assistant"
    )


    print(
        manager.get_all_prompts()
    )
