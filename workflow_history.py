"""
DG AI Version 1
Workflow History

Purpose:
- Store workflow execution records
- Track workflow changes
- Maintain workflow history

Version: 1.0
"""

import logging
from datetime import datetime


class WorkflowHistory:
    """
    Professional Workflow History Manager
    """

    def __init__(self):

        self.history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def add_record(
        self,
        workflow_name,
        status,
        details=None
    ):
        """
        Add workflow history record.
        """

        record = {

            "workflow":
            workflow_name,

            "status":
            status,

            "details":
            details,

            "time":
            str(datetime.now())

        }


        self.history.append(
            record
        )


        return record


    # ---------------------------------

    def get_history(self):
        """
        Return all workflow history.
        """

        return self.history


    # ---------------------------------

    def get_workflow_history(
        self,
        workflow_name
    ):
        """
        Get specific workflow records.
        """

        result = []


        for record in self.history:

            if record["workflow"] == workflow_name:

                result.append(record)


        return result


    # ---------------------------------

    def search_history(
        self,
        keyword
    ):
        """
        Search workflow records.
        """

        result = []


        for record in self.history:

            if keyword.lower() in str(record).lower():

                result.append(record)


        return result


    # ---------------------------------

    def clear_history(self):
        """
        Clear workflow history.
        """

        self.history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    history = WorkflowHistory()


    history.add_record(
        "AI Automation",
        "completed",
        "Workflow finished"
    )


    print(
        history.get_history()
    )
