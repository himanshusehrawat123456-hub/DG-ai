"""
DG AI Version 1
User Data Refiner

Purpose:
- Clean user data
- Remove unwanted values
- Improve stored information

Version: 1.0
"""

import logging
from datetime import datetime


class UserRefiner:

    def __init__(self):

        self.history = []

        logging.basicConfig(
            level=logging.INFO
        )


    def clean_data(
        self,
        data
    ):

        cleaned = {}

        for key, value in data.items():

            if value not in [
                "",
                None
            ]:

                cleaned[key] = value


        self.save_history(
            "data_cleaned"
        )


        return cleaned


    def remove_duplicate_values(
        self,
        data
    ):

        result = {}

        seen = set()


        for key, value in data.items():

            if value not in seen:

                result[key] = value

                seen.add(value)


        self.save_history(
            "duplicate_removed"
        )


        return result


    def refine_user_data(
        self,
        data
    ):

        data = self.clean_data(
            data
        )

        data = self.remove_duplicate_values(
            data
        )

        return data


    def save_history(
        self,
        action
    ):

        self.history.append({

            "action": action,

            "time":
            str(datetime.now())

        })


    def get_history(self):

        return self.history



if __name__ == "__main__":

    refiner = UserRefiner()

    print(
        refiner.refine_user_data(
            {
                "name": "DG AI",
                "empty": "",
                "type": "AI"
            }
        )
    )
