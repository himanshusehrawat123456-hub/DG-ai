"""
DG AI Version 1
Command Router System

Purpose:
- Route user commands
- Connect commands with modules
- Provide command handling foundation

Version: 1.0
"""


class CommandRouter:
    """
    Handles DG AI command routing.
    """



    def __init__(self):

        self.routes = {}



    def add_route(self, command, module):
        """
        Add command route.
        """

        self.routes[command] = module


        return True



    def route_command(self, command):
        """
        Find module for command.
        """

        for key in self.routes:

            if key in command.lower():

                return self.routes[key]


        return "No module found"



    def get_routes(self):
        """
        Return all routes.
        """

        return self.routes




# Testing

if __name__ == "__main__":


    router = CommandRouter()


    router.add_route(
        "voice",
        "voice_manager"
    )


    router.add_route(
        "file",
        "file_manager"
    )


    print(
        router.route_command(
            "open voice system"
        )
    )


    print(
        router.get_routes()
    )
