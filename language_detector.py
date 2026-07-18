"""
DG AI Version 1
Language Detector

Purpose:
- Detect input language
- Store detection results
- Provide language information

Version: 1.0
"""

import logging
from datetime import datetime


class LanguageDetector:
    """
    Professional Language Detection System
    """

    def __init__(self):

        self.detection_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def detect_language(
        self,
        text
    ):
        """
        Detect language from text.
        """

        if not text:

            return {

                "language": "unknown",

                "confidence": 0

            }


        if any(
            char in text
            for char in "अआइईउऊएऐओऔकखगघचछजटठडढतथदधनपफबभमययरलवशषसह"
        ):

            language = "Hindi"

            confidence = 0.95


        elif all(
            ord(char) < 128
            for char in text
            if char.isalpha()
        ):

            language = "English"

            confidence = 0.90


        else:

            language = "Unknown"

            confidence = 0.50



        record = {

            "text":
            text,

            "language":
            language,

            "confidence":
            confidence,

            "time":
            str(datetime.now())

        }


        self.detection_history.append(
            record
        )


        return record


    # ---------------------------------

    def get_history(self):

        return self.detection_history


    # ---------------------------------

    def clear_history(self):

        self.detection_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    detector = LanguageDetector()


    print(
        detector.detect_language(
            "नमस्ते DG AI"
        )
    )
