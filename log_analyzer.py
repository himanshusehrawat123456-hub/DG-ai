"""
DG AI Version 1
Log Analyzer

Purpose:
- Analyze application logs
- Count errors and warnings
- Generate log reports
- Provide monitoring foundation

Version: 1.0
"""

import logging
from datetime import datetime


class LogAnalyzer:
    """
    Professional Log Analysis Engine
    """

    def __init__(self):

        self.analysis_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def count_level(self, logs, level):
        """
        Count logs by level.
        """

        count = 0

        for log in logs:

            if level.lower() in log.lower():

                count += 1


        return count


    # ---------------------------------

    def find_errors(self, logs):
        """
        Find error messages.
        """

        errors = []

        for log in logs:

            if "error" in log.lower():

                errors.append(log)


        return errors


    # ---------------------------------

    def find_warnings(self, logs):
        """
        Find warning messages.
        """

        warnings = []

        for log in logs:

            if "warning" in log.lower():

                warnings.append(log)


        return warnings


    # ---------------------------------

    def generate_report(self, logs):
        """
        Generate complete log report.
        """

        report = {

            "total_logs":
            len(logs),

            "errors":
            self.count_level(
                logs,
                "error"
            ),

            "warnings":
            self.count_level(
                logs,
                "warning"
            ),

            "created_at":
            str(datetime.now())

        }


        self.analysis_history.append(
            report
        )


        logging.info(
            "Log report generated"
        )


        return report


    # ---------------------------------

    def get_history(self):
        """
        Return analysis history.
        """

        return self.analysis_history


    # ---------------------------------

    def clear_history(self):
        """
        Clear reports.
        """

        self.analysis_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    analyzer = LogAnalyzer()


    sample_logs = [

        "INFO Application Started",

        "WARNING Low Memory",

        "ERROR Database Failed",

        "INFO Task Completed"

    ]


    print(
        analyzer.generate_report(
            sample_logs
        )
    )
