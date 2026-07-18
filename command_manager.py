"""
DG AI Version 1
Command Manager

Purpose:
- Manage AI commands
- Register commands
- Control command execution flow

Version: 1.0
"""

import logging
from datetime import datetime


class CommandManager:
    """
    Professional AI Command Manager
    """

    def __init__(self):

        self.commands = {}

        self.command_logs = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def register_command(
        self,
        name,
        function
    ):
        """
        Register new command.
        """

        self.commands[name] = function


        self.log_command(
            name,
            "registered"
        )


        return True


    # ---------------------------------

    def remove_command(
        self,
        name
    ):
        """
        Remove command.
        """

        if name in self.commands:

            del self.commands[name]

            self.log_command(
                name,
                "removed"
            )

            return True


        return False


    # ---------------------------------

    def execute_command(
        self,
        name,
        *args,
        **kwargs
    ):
        """
        Execute registered command.
        """

        if name not in self.commands:

            return {

                "status": "failed",

                "message": "Command not found"

            }


        try:

            result = self.commands[name](
                *args,
                **kwargs
            )


            self.log_command(
                name,
                "executed"
            )


            return {

                "status": "success",

                "result": result

            }


        except Exception as error:

            return {

                "status": "error",

                "message": str(error)

            }


    # ---------------------------------

    def get_commands(self):
        """
        Return available commands.
        """

        return list(
            self.commands.keys()
        )


    # ---------------------------------

    def log_command(
        self,
        command,
        action
    ):

        self.command_logs.append({

            "command": command,

            "action": action,

            "time": str(datetime.now())

        })


    # ---------------------------------

    def get_logs(self):

        return self.command_logs


    # ---------------------------------

    def clear_logs(self):

        self.command_logs.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    manager = CommandManager()


    def hello():

        return "Hello DG AI"


    manager.register_command(
        "hello",
        hello
    )


    print(
        manager.execute_command(
            "hello"
        )
    )
