"""
DG AI Version 1
Environment Manager

Purpose:
- Manage application environment settings

Version: 1.0
"""


import os



class EnvironmentManager:
    """
    Handles environment variables.
    """



    def __init__(self):

        self.environment = {}



    def set_variable(self, key, value):
        """
        Set environment value.
        """

        self.environment[key] = value

        return True



    def get_variable(self, key):
        """
        Get environment value.
        """

        return self.environment.get(key)



    def get_all_variables(self):
        """
        Return all variables.
        """

        return self.environment




# Testing

if __name__ == "__main__":


    env = EnvironmentManager()


    env.set_variable(
        "MODE",
        "Development"
    )


    print(
        env.get_all_variables()
    )
