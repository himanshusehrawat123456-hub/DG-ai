"""
DG AI Version 1
Health Checker

Purpose:
- Check health of DG AI modules
- Store health reports

Version: 1.0
"""

import datetime


class HealthChecker:
    """
    Handles health checking.
    """

    def __init__(self):
        self.health_reports = []

    def check_module(self, module_name, status):
        """
        Check module health.
        """

        report = {
            "id": len(self.health_reports) + 1,
            "module": module_name,
            "status": status,
            "checked_at": str(datetime.datetime.now())
        }

        self.health_reports.append(report)

        return report

    def get_reports(self):
        """
        Return all health reports.
        """

        return self.health_reports

    def clear_reports(self):
        """
        Clear all health reports.
        """

        self.health_reports.clear()

        return True


# Testing

if __name__ == "__main__":

    checker = HealthChecker()

    print(
        checker.check_module(
            "Memory System",
            "Healthy"
        )
    )

    print(
        checker.get_reports()
    )
