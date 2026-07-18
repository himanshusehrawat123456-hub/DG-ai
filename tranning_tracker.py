"""
DG AI Version 1
Training Tracker System

Purpose:
- Track learning progress
- Manage training records

Version: 1.0
"""


import datetime



class TrainingTracker:
    """
    Handles training tracking operations.
    """



    def __init__(self):

        self.training_records = []



    def add_training(self, topic, progress):
        """
        Add training record.
        """

        record = {

            "id":
            len(self.training_records) + 1,

            "topic":
            topic,

            "progress":
            progress,

            "date":
            str(datetime.datetime.now())

        }


        self.training_records.append(record)


        return True



    def update_progress(self, topic, progress):
        """
        Update topic progress.
        """

        for record in self.training_records:

            if record["topic"] == topic:

                record["progress"] = progress

                return True


        return False



    def get_training_records(self):
        """
        Return all training records.
        """

        return self.training_records



    def clear_records(self):
        """
        Clear training data.
        """

        self.training_records.clear()

        return True




# Testing

if __name__ == "__main__":


    tracker = TrainingTracker()


    tracker.add_training(
        "Python",
        "50% Complete"
    )


    tracker.update_progress(
        "Python",
        "100% Complete"
    )


    print(
        tracker.get_training_records()
    )
