"""
DG AI Version 1
Command Executor

Purpose:
- Execute processed commands
- Connect commands with actions
- Maintain execution records

Version: 1.0
"""

import logging
from datetime import datetime


class CommandExecutor:
    """
    Professional AI Command Executor
    """

    def __init__(self):

        self.executed_commands = []

        self.available_actions = {}

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def register_action(
        self,
        command,
        action
    ):
        """
        Register command action.
        """

        self.available_actions[command] = action


        return True


    # ---------------------------------

    def execute(
        self,
        parsed_command
    ):
        """
        Execute parsed command.
        """

        if not parsed_command:

            return {

                "status": "failed",

                "message": "Invalid command"

            }


        command_name = parsed_command.get(
            "command"
        )


        arguments = parsed_command.get(
            "arguments",
            []
        )


        if command_name not in self.available_actions:

            return {

                "status": "failed",

                "message": "Action not found"

            }


        try:

            result = self.available_actions[command_name](
                *arguments
            )


            record = {

                "command": command_name,

                "arguments": arguments,

                "result": result,

                "time": str(datetime.now())

            }


            self.executed_commands.append(
                record
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

    def get_actions(self):

        return list(
            self.available_actions.keys()
        )


    # ---------------------------------

    def get_history(self):

        return self.executed_commands


    # ---------------------------------

    def clear_history(self):

        self.executed_commands.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    executor = CommandExecutor()


    def hello():

        return "DG AI Ready"


    executor.register_action(
        "hello",
        hello
    )


    print(
        executor.execute(
            {
                "command": "hello",
                "arguments": []
            }
        )
    )
