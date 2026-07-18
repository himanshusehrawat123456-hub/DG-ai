"""
DG AI Version 1
Data Converter

Purpose:
- Convert data between formats
- Support JSON, CSV and Text conversion
- Provide conversion history

Version: 1.0
"""

import json
import csv
import os
import logging
from datetime import datetime


class DataConverter:
    """
    Professional Data Conversion Engine
    """

    def __init__(self):

        self.history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def save_history(self, action, source, result):

        record = {

            "action": action,

            "source": source,

            "result": result,

            "time": str(datetime.now())

        }

        self.history.append(record)


    # ---------------------------------

    def dict_to_json(
        self,
        data,
        file_name="data.json"
    ):
        """
        Convert dictionary to JSON file.
        """

        try:

            with open(
                file_name,
                "w"
            ) as file:

                json.dump(
                    data,
                    file,
                    indent=4
                )


            self.save_history(
                "JSON Export",
                data,
                file_name
            )


            return True


        except Exception as error:

            logging.error(error)

            return False


    # ---------------------------------

    def json_to_dict(
        self,
        file_name
    ):
        """
        Read JSON file.
        """

        try:

            with open(
                file_name,
                "r"
            ) as file:

                data = json.load(file)


            self.save_history(
                "JSON Import",
                file_name,
                data
            )


            return data


        except Exception as error:

            logging.error(error)

            return None


    # ---------------------------------

    def list_to_csv(
        self,
        data,
        file_name="data.csv"
    ):
        """
        Convert list data to CSV.
        """

        try:

            if len(data) == 0:

                return False


            keys = data[0].keys()


            with open(
                file_name,
                "w",
                newline=""
            ) as file:


                writer = csv.DictWriter(
                    file,
                    fieldnames=keys
                )


                writer.writeheader()

                writer.writerows(
                    data
                )


            self.save_history(
                "CSV Export",
                data,
                file_name
            )


            return True


        except Exception as error:

            logging.error(error)

            return False


    # ---------------------------------

    def text_to_data(
        self,
        text
    ):
        """
        Convert text into line data.
        """

        result = text.splitlines()


        self.save_history(
            "Text Convert",
            text,
            result
        )


        return result


    # ---------------------------------

    def check_file(self, file_name):
        """
        Check file availability.
        """

        return os.path.exists(
            file_name
        )


    # ---------------------------------

    def get_history(self):
        """
        Return conversion history.
        """

        return self.history


    # ---------------------------------

    def clear_history(self):
        """
        Clear conversion history.
        """

        self.history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    converter = DataConverter()


    sample = {

        "name": "DG AI",

        "version": "1.0"

    }


    print(
        converter.dict_to_json(
            sample
        )
    )


    print(
        converter.get_history()
    )
