"""
DG AI Version 1
Voice Generator

Purpose:
- Convert text into voice output
- Manage voice generation requests
- Store generated voice records

Version: 1.0
"""

import logging
from datetime import datetime


class VoiceGenerator:
    """
    Professional Voice Generation System
    """

    def __init__(self):

        self.voice_records = []

        self.supported_voices = [

            "default",
            "male",
            "female"

        ]


        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def generate_voice(
        self,
        text,
        voice_type="default"
    ):
        """
        Generate voice from text.
        """

        if voice_type not in self.supported_voices:

            voice_type = "default"


        record = {

            "id":
            len(self.voice_records) + 1,

            "text":
            text,

            "voice":
            voice_type,

            "status":
            "generated",

            "audio_file":
            f"voice_{len(self.voice_records)+1}.wav",

            "time":
            str(datetime.now())

        }


        self.voice_records.append(
            record
        )


        return record


    # ---------------------------------

    def add_voice_type(
        self,
        voice_type
    ):

        if voice_type not in self.supported_voices:

            self.supported_voices.append(
                voice_type
            )

            return True


        return False


    # ---------------------------------

    def get_records(self):

        return self.voice_records


    # ---------------------------------

    def clear_records(self):

        self.voice_records.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    generator = VoiceGenerator()


    print(
        generator.generate_voice(
            "Hello, I am DG AI"
        )
    )
