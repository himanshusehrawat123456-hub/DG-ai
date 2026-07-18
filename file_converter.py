"""
DG AI Version 1
File Converter System

Purpose:
- Convert file formats
- Manage conversion requests

Version: 1.0
"""


import datetime



class FileConverter:
    """
    Handles file conversion operations.
    """



    def __init__(self):

        self.conversions = []



    def convert_file(self, source, target):
        """
        Create conversion record.
        """

        conversion = {

            "id":
            len(self.conversions) + 1,

            "source":
            source,

            "target":
            target,

            "status":
            "Converted",

            "time":
            str(datetime.datetime.now())

        }


        self.conversions.append(conversion)


        return conversion



    def get_history(self):
        """
        Return conversion history.
        """

        return self.conversions



    def clear_history(self):
        """
        Clear conversion history.
        """

        self.conversions.clear()

        return True




# Testing

if __name__ == "__main__":


    converter = FileConverter()


    print(
        converter.convert_file(
            "file.txt",
            "file.pdf"
        )
    )
