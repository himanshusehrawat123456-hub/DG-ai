"""
DG AI Version 1
Document Converter

Purpose:
- Convert document formats
- Manage conversion records
- Provide conversion foundation

Version: 1.0
"""

import os
import shutil
import logging
from datetime import datetime


class DocumentConverter:
    """
    Professional Document Converter
    """

    def __init__(self):

        self.conversion_history = []

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
        Check file availability.
        """

        return os.path.exists(
            file_path
        )


    # ---------------------------------

    def convert_file(
        self,
        source,
        destination
    ):
        """
        Basic file conversion foundation.
        """

        try:

            if not self.check_file(
                source
            ):

                return {

                    "status": "failed",

                    "message": "Source file not found"

                }


            shutil.copy(
                source,
                destination
            )


            record = {

                "source": source,

                "destination": destination,

                "status": "converted",

                "time": str(datetime.now())

            }


            self.conversion_history.append(
                record
            )


            return record


        except Exception as error:

            return {

                "status": "failed",

                "error": str(error)

            }


    # ---------------------------------

    def get_extension(
        self,
        file_path
    ):
        """
        Get file extension.
        """

        return os.path.splitext(
            file_path
        )[1]


    # ---------------------------------

    def supported_formats(self):

        return [

            "txt",

            "pdf",

            "docx",

            "json"

        ]


    # ---------------------------------

    def get_history(self):

        return self.conversion_history


    # ---------------------------------

    def clear_history(self):

        self.conversion_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    converter = DocumentConverter()

    print(
        converter.supported_formats()
    )
