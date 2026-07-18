"""
DG AI Version 1
Workflow Executor

Purpose:
- Execute workflow steps
- Run automated tasks
- Track execution status

Version: 1.0
"""

import logging
from datetime import datetime


class WorkflowExecutor:
    """
    Professional Workflow Executor
    """

    def __init__(self):

        self.executions = []

        self.actions = {}

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def register_action(
        self,
        action_name,
        function
    ):
        """
        Register workflow action.
        """

        self.actions[action_name] = function

        return True


    # ---------------------------------

    def execute_workflow(
        self,
        workflow
    ):
        """
        Execute complete workflow.
        """

        if not workflow:

            return {

                "status": "failed",

                "message": "Workflow not found"

            }


        results = []


        for step in workflow.get(
            "steps",
            []
        ):

            action = step.get(
                "action"
            )


            if action in self.actions:

                try:

                    result = self.actions[action]()

                    results.append({

                        "step": step["step"],

                        "status": "completed",

                        "result": result

                    })


                except Exception as error:

                    results.append({

                        "step": step["step"],

                        "status": "error",

                        "message": str(error)

                    })


            else:

                results.append({

                    "step": step["step"],

                    "status": "skipped",

                    "message": "Action not registered"

                })


        record = {

            "workflow":
            workflow.get("name"),

            "results":
            results,

            "time":
            str(datetime.now())

        }


        self.executions.append(
            record
        )


        return record


    # ---------------------------------

    def get_actions(self):

        return list(
            self.actions.keys()
        )


    # ---------------------------------

    def get_execution_history(self):

        return self.executions


    # ---------------------------------

    def clear_history(self):

        self.executions.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    executor = WorkflowExecutor()


    executor.register_action(
        "hello",
        lambda: "DG AI Running"
    )


    workflow = {

        "name": "Test Workflow",

        "steps": [

            {
                "step": "Start",
                "action": "hello"
            }

        ]

    }


    print(
        executor.execute_workflow(
            workflow
        )
    )
