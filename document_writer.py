"""
DG AI Version 1
Document Writer

Purpose:
- Create documents
- Write and update files
- Maintain writing history

Version: 1.0
"""

import os
import logging
from datetime import datetime


class DocumentWriter:
    """
    Professional Document Writer
    """

    def __init__(self):

        self.write_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def create_document(
        self,
        file_path,
        content=""
    ):
        """
        Create new document.
        """

        try:

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    content
                )


            self.log_action(
                file_path,
                "created"
            )


            return True


        except Exception as error:

            return {

                "error": str(error)

            }


    # ---------------------------------

    def write_document(
        self,
        file_path,
        content
    ):
        """
        Write content to document.
        """

        try:

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    content
                )


            self.log_action(
                file_path,
                "written"
            )


            return True


        except Exception as error:

            return {

                "error": str(error)

            }


    # ---------------------------------

    def append_document(
        self,
        file_path,
        content
    ):
        """
        Add content to existing document.
        """

        try:

            with open(
                file_path,
                "a",
                encoding="utf-8"
            ) as file:

                file.write(
                    content
                )


            self.log_action(
                file_path,
                "appended"
            )


            return True


        except Exception as error:

            return {

                "error": str(error)

            }


    # ---------------------------------

    def update_document(
        self,
        file_path,
        old_text,
        new_text
    ):
        """
        Replace document content.
        """

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                data = file.read()


            data = data.replace(
                old_text,
                new_text
            )


            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(
                    data
                )


            self.log_action(
                file_path,
                "updated"
            )


            return True


        except Exception:

            return False


    # ---------------------------------

    def log_action(
        self,
        file_path,
        action
    ):

        self.write_history.append({

            "file": file_path,

            "action": action,

            "time": str(datetime.now())

        })


    # ---------------------------------

    def get_history(self):

        return self.write_history


    # ---------------------------------

    def clear_history(self):

        self.write_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    writer = DocumentWriter()

    writer.create_document(
        "test.txt",
        "DG AI Document"
    )

    print(
        writer.get_history()
    )
