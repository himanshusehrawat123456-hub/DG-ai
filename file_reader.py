"""
DG AI Version 1
File Reader System

Purpose:
- Read file data
- Handle file reading operations

Version: 1.0
"""


import os



class FileReader:
    """
    Handles file reading.
    """



    def read_file(self, file_path):
        """
        Read text file.
        """

        try:

            with open(
                file_path,
                "r",
                encoding="utf-8"
            ) as file:

                return file.read()


        except Exception as error:

            return str(error)



    def file_exists(self, file_path):
        """
        Check file existence.
        """

        return os.path.exists(file_path)




# Testing

if __name__ == "__main__":


    reader = FileReader()


    print(
        reader.file_exists(
            "test.txt"
        )
    )
