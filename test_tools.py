"""
DG AI Version 1
Tools Testing System

Purpose:
- Test DG AI tools
- Check tool modules working

Version: 1.0
"""


import datetime



class ToolTester:
    """
    Handles tools testing.
    """



    def __init__(self):

        self.results = []



    def run_test(self, tool_name, status):
        """
        Store test result.
        """

        result = {

            "tool":
            tool_name,

            "status":
            status,

            "time":
            str(datetime.datetime.now())

        }


        self.results.append(result)


        return result



    def get_results(self):
        """
        Return all test results.
        """

        return self.results



    def clear_results(self):
        """
        Clear testing history.
        """

        self.results.clear()

        return True




# Testing

if __name__ == "__main__":


    tester = ToolTester()


    tester.run_test(
        "Calculator Tool",
        "Passed"
    )


    tester.run_test(
        "System Tool",
        "Passed"
    )


    print(
        tester.get_results()
    )
