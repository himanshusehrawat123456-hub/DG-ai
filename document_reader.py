"""
DG AI Version 1
Document Reader

Purpose:
- Read document files
- Extract text data
- Maintain reading history

Version: 1.0
"""

import os
import logging
from datetime import datetime


class DocumentReader:
    """
    Professional Document Reader
    """

    def __init__(self):

        self.read_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def check_file(
        self,
        file_path
    ):
        """
        Check file exists.
        """

        return os.path.exists(
            file_path
        )


    # ---------------------------------

    def read_text_file(
        self,
        file_path
    ):
        """
        Read text document.
        """

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                content = file.read()


            self.save_history(
                file_path,
                "text_read"
            )


            return content


        except Exception as error:

            return {

                "error": str(error)

            }


    # ---------------------------------

    def read_lines(
        self,
        file_path
    ):
        """
        Read document lines.
        """

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                lines = file.readlines()


            self.save_history(
                file_path,
                "line_read"
            )


            return lines


        except Exception as error:

            return {

                "error": str(error)

            }


    # ---------------------------------

    def get_word_count(
        self,
        text
    ):
        """
        Count words.
        """

        return len(
            text.split()
        )


    # ---------------------------------

    def save_history(
        self,
        file_path,
        action
    ):

        self.read_history.append({

            "file": file_path,

            "action": action,

            "time": str(datetime.now())

        })


    # ---------------------------------

    def get_history(self):

        return self.read_history
