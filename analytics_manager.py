"""
DG AI Version 1
Analytics Manager System

Purpose:
- Manage analytics data
- Store system metrics

Version: 1.0
"""


import datetime



class AnalyticsManager:
    """
    Handles analytics operations.
    """



    def __init__(self):

        self.metrics = []



    def add_metric(self, name, value):
        """
        Add analytics metric.
        """

        metric = {

            "id":
            len(self.metrics) + 1,

            "name":
            name,

            "value":
            value,

            "time":
            str(datetime.datetime.now())

        }


        self.metrics.append(metric)


        return metric



    def get_metrics(self):
        """
        Return all metrics.
        """

        return self.metrics



    def clear_metrics(self):
        """
        Clear analytics data.
        """

        self.metrics.clear()

        return True




# Testing

if __name__ == "__main__":


    analytics = AnalyticsManager()


    print(
        analytics.add_metric(
            "User Activity",
            100
        )
    )
