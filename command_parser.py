"""
DG AI Version 1
Command Parser

Purpose:
- Understand user commands
- Extract command name and arguments
- Prepare commands for execution

Version: 1.0
"""

import logging
from datetime import datetime


class CommandParser:
    """
    Professional AI Command Parser
    """

    def __init__(self):

        self.parsed_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def clean_command(
        self,
        command
    ):
        """
        Clean user input.
        """

        if not isinstance(
            command,
            str
        ):

            return ""


        return command.strip().lower()


    # ---------------------------------

    def parse(
        self,
        command
    ):
        """
        Parse command into parts.
        """

        cleaned = self.clean_command(
            command
        )


        if not cleaned:

            return None


        parts = cleaned.split()


        result = {

            "command":
            parts[0],

            "arguments":
            parts[1:],

            "original":
            command,

            "time":
            str(datetime.now())

        }


        self.parsed_history.append(
            result
        )


        return result


    # ---------------------------------

    def get_command_name(
        self,
        parsed_data
    ):
        """
        Get command name.
        """

        if parsed_data:

            return parsed_data.get(
                "command"
            )


        return None


    # ---------------------------------

    def get_arguments(
        self,
        parsed_data
    ):
        """
        Get command arguments.
        """

        if parsed_data:

            return parsed_data.get(
                "arguments"
            )


        return []


    # ---------------------------------

    def get_history(self):

        return self.parsed_history


    # ---------------------------------

    def clear_history(self):

        self.parsed_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    parser = CommandParser()


    result = parser.parse(
        "open file test.txt"
    )


    print(result)
