"""
DG AI Version 1
Translator Engine

Purpose:
- Process translation requests
- Manage translation logic
- Provide translated output

Version: 1.0
"""

import logging
from datetime import datetime


class TranslatorEngine:
    """
    Professional Translation Engine
    """

    def __init__(self):

        self.languages = [

            "English",
            "Hindi",
            "Spanish",
            "French",
            "German"

        ]

        self.translation_history = []


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def add_language(
        self,
        language
    ):
        """
        Add supported language.
        """

        if language not in self.languages:

            self.languages.append(
                language
            )

            return True


        return False


    # ---------------------------------

    def translate_text(
        self,
        text,
        source,
        target
    ):
        """
        Translate text.
        """

        if target not in self.languages:

            return {

                "status":
                "failed",

                "message":
                "Language not supported"

            }


        result = {

            "source":
            source,

            "target":
            target,

            "original":
            text,

            "translated":
            f"{target}: {text}",

            "time":
            str(datetime.now())

        }


        self.translation_history.append(
            result
        )


        return result


    # ---------------------------------

    def get_languages(self):

        return self.languages


    # ---------------------------------

    def get_history(self):

        return self.translation_history


    # ---------------------------------

    def clear_history(self):

        self.translation_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    engine = TranslatorEngine()


    print(
        engine.translate_text(
            "Hello",
            "English",
            "Hindi"
        )
    )
