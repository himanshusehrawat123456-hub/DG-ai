"""
DG AI Version 1
Audio Manager System

Purpose:
- Manage audio files
- Store audio information

Version: 1.0
"""


import datetime



class AudioManager:
    """
    Handles audio management.
    """



    def __init__(self):

        self.audio_files = []



    def add_audio(self, name, path):
        """
        Add audio record.
        """

        audio = {

            "id":
            len(self.audio_files) + 1,

            "name":
            name,

            "path":
            path,

            "time":
            str(datetime.datetime.now())

        }


        self.audio_files.append(audio)


        return audio



    def get_audio_files(self):
        """
        Return audio list.
        """

        return self.audio_files



    def remove_audio(self, audio_id):
        """
        Remove audio record.
        """

        for audio in self.audio_files:

            if audio["id"] == audio_id:

                self.audio_files.remove(audio)

                return True


        return False




# Testing

if __name__ == "__main__":


    manager = AudioManager()


    print(
        manager.add_audio(
            "voice.mp3",
            "/audio/voice.mp3"
        )
    )
