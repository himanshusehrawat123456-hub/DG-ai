"""
DG AI Version 1
File Writer System

Purpose:
- Write data into files
- Handle file creation operations

Version: 1.0
"""


import os



class FileWriter:
    """
    Handles file writing.
    """



    def write_file(self, file_path, data):
        """
        Write data to file.
        """

        try:

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as file:

                file.write(data)


            return True


        except Exception as error:

            return str(error)



    def append_file(self, file_path, data):
        """
        Append data to existing file.
        """

        try:

            with open(
                file_path,
                "a",
                encoding="utf-8"
            ) as file:

                file.write(data)


            return True


        except Exception as error:

            return str(error)



    def create_file(self, file_path):
        """
        Create empty file.
        """

        try:

            open(
                file_path,
                "w"
            ).close()


            return True


        except Exception as error:

            return str(error)




# Testing

if __name__ == "__main__":


    writer = FileWriter()


    writer.write_file(
        "test.txt",
        "Hello DG AI"
    )


    print("File Written")
