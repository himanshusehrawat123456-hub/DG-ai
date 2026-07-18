"""
DG AI Version 1
Report Generator System

Purpose:
- Generate analytics reports
- Manage report records

Version: 1.0
"""


import datetime



class ReportGenerator:
    """
    Handles report generation.
    """



    def __init__(self):

        self.reports = []



    def create_report(self, title, data):
        """
        Create new report.
        """

        report = {

            "id":
            len(self.reports) + 1,

            "title":
            title,

            "data":
            data,

            "status":
            "Generated",

            "time":
            str(datetime.datetime.now())

        }


        self.reports.append(report)


        return report



    def get_reports(self):
        """
        Return all reports.
        """

        return self.reports



    def delete_report(self, report_id):
        """
        Delete report.
        """

        for report in self.reports:

            if report["id"] == report_id:

                self.reports.remove(report)

                return True


        return False




# Testing

if __name__ == "__main__":


    generator = ReportGenerator()


    print(
        generator.create_report(
            "DG AI Usage Report",
            {
                "users": 100
            }
        )
    )
