"""
DG AI Version 1
Performance Monitor System

Purpose:
- Monitor system performance
- Track execution metrics

Version: 1.0
"""


import datetime



class PerformanceMonitor:
    """
    Handles performance monitoring.
    """



    def __init__(self):

        self.records = []



    def record_performance(self, module, response_time):
        """
        Record module performance.
        """

        data = {

            "id":
            len(self.records) + 1,

            "module":
            module,

            "response_time":
            response_time,

            "time":
            str(datetime.datetime.now())

        }


        self.records.append(data)


        return True



    def get_performance(self):
        """
        Return performance records.
        """

        return self.records



    def clear_records(self):
        """
        Clear performance data.
        """

        self.records.clear()

        return True




# Testing

if __name__ == "__main__":


    monitor = PerformanceMonitor()


    monitor.record_performance(
        "AI Core",
        "0.5 seconds"
    )


    print(
        monitor.get_performance()
    )
