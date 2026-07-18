"""
DG AI Version 1
Translation History

Purpose:
- Store translation records
- Track translation activities
- Maintain translation audit history

Version: 1.0
"""

import logging
from datetime import datetime


class TranslationHistory:
    """
    Professional Translation History Manager
    """

    def __init__(self):

        self.records = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def add_record(
        self,
        original_text,
        translated_text,
        source_language,
        target_language
    ):
        """
        Add translation history record.
        """

        record = {

            "id":
            len(self.records) + 1,

            "original":
            original_text,

            "translated":
            translated_text,

            "source":
            source_language,

            "target":
            target_language,

            "time":
            str(datetime.now())

        }


        self.records.append(
            record
        )


        return record


    # ---------------------------------

    def get_history(self):
        """
        Return all translation history.
        """

        return self.records


    # ---------------------------------

    def search_history(
        self,
        keyword
    ):
        """
        Search translation records.
        """

        result = []


        for record in self.records:

            if keyword.lower() in str(record).lower():

                result.append(record)


        return result


    # ---------------------------------

    def get_by_language(
        self,
        language
    ):
        """
        Get records by target language.
        """

        return [

            record for record in self.records

            if record["target"] == language

        ]


    # ---------------------------------

    def clear_history(self):

        self.records.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    history = TranslationHistory()


    history.add_record(
        "Hello",
        "नमस्ते",
        "English",
        "Hindi"
    )


    print(
        history.get_history()
    )
