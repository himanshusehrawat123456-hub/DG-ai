"""
DG AI Version 1
Workflow Builder

Purpose:
- Create workflows
- Add workflow steps
- Manage workflow structure

Version: 1.0
"""

import logging
from datetime import datetime


class WorkflowBuilder:
    """
    Professional Workflow Builder
    """

    def __init__(self):

        self.workflows = {}

        self.history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def create_workflow(
        self,
        workflow_id,
        name
    ):
        """
        Create new workflow.
        """

        workflow = {

            "id": workflow_id,

            "name": name,

            "steps": [],

            "created": str(datetime.now())

        }


        self.workflows[workflow_id] = workflow


        self.log_action(
            workflow_id,
            "created"
        )


        return workflow


    # ---------------------------------

    def add_step(
        self,
        workflow_id,
        step_name,
        action
    ):
        """
        Add step to workflow.
        """

        if workflow_id not in self.workflows:

            return False


        step = {

            "step": step_name,

            "action": action,

            "added": str(datetime.now())

        }


        self.workflows[workflow_id]["steps"].append(
            step
        )


        self.log_action(
            workflow_id,
            "step_added"
        )


        return True


    # ---------------------------------

    def remove_step(
        self,
        workflow_id,
        step_name
    ):
        """
        Remove workflow step.
        """

        if workflow_id not in self.workflows:

            return False


        steps = self.workflows[workflow_id]["steps"]


        for step in steps:

            if step["step"] == step_name:

                steps.remove(step)

                return True


        return False


    # ---------------------------------

    def get_workflow(
        self,
        workflow_id
    ):

        return self.workflows.get(
            workflow_id
        )


    # ---------------------------------

    def get_all_workflows(self):

        return self.workflows


    # ---------------------------------

    def log_action(
        self,
        workflow_id,
        action
    ):

        self.history.append({

            "workflow": workflow_id,

            "action": action,

            "time": str(datetime.now())

        })


    # ---------------------------------

    def get_history(self):

        return self.history



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    builder = WorkflowBuilder()


    builder.create_workflow(
        1,
        "AI Automation"
    )


    builder.add_step(
        1,
        "Search Data",
        "search"
    )


    print(
        builder.get_workflow(1)
    )
