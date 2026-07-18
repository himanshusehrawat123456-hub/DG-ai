"""
DG AI Version 1
Log Archiver

Purpose:
- Archive old log files
- Keep archive history

Version: 1.0
"""

import os
import shutil
import datetime


class LogArchiver:
    """
    Handles log archiving.
    """

    def __init__(
        self,
        log_file="dg_ai.log",
        archive_folder="log_archive"
    ):

        self.log_file = log_file
        self.archive_folder = archive_folder

        os.makedirs(
            self.archive_folder,
            exist_ok=True
        )



    def archive_logs(self):
        """
        Archive the current log file.
        """

        if not os.path.exists(self.log_file):

            return False


        timestamp = datetime.datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        archive_name = (
            f"dg_ai_{timestamp}.log"
        )

        destination = os.path.join(
            self.archive_folder,
            archive_name
        )

        shutil.copy2(
            self.log_file,
            destination
        )

        return destination



    def list_archives(self):
        """
        Return archived log files.
        """

        return os.listdir(
            self.archive_folder
        )


# Testing

if __name__ == "__main__":

    archiver = LogArchiver()

    print(
        archiver.archive_logs()
    )

    print(
        archiver.list_archives()
    )
