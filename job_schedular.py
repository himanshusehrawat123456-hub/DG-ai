"""
DG AI Version 1
Job Scheduler

Purpose:
- Schedule and execute jobs
- Manage scheduled tasks
- Track job status

Version: 1.0
"""

import logging
from datetime import datetime


class JobScheduler:
    """
    Professional Job Scheduler
    """

    def __init__(self):

        self.jobs = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def add_job(
        self,
        job_name,
        function,
        run_time
    ):
        """
        Add new scheduled job.
        """

        job = {

            "id":
            len(self.jobs) + 1,

            "name":
            job_name,

            "function":
            function,

            "run_time":
            run_time,

            "status":
            "pending",

            "created":
            str(datetime.now())

        }


        self.jobs.append(job)

        return job


    # ---------------------------------

    def run_job(
        self,
        job_id
    ):
        """
        Execute scheduled job.
        """

        for job in self.jobs:

            if job["id"] == job_id:

                try:

                    result = job["function"]()

                    job["status"] = "completed"

                    job["result"] = result

                    job["completed"] = str(
                        datetime.now()
                    )

                    return result


                except Exception as error:

                    job["status"] = "failed"

                    job["error"] = str(error)

                    return None


        return False


    # ---------------------------------

    def get_jobs(self):

        return self.jobs


    # ---------------------------------

    def remove_job(
        self,
        job_id
    ):

        for job in self.jobs:

            if job["id"] == job_id:

                self.jobs.remove(job)

                return True


        return False



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    scheduler = JobScheduler()


    scheduler.add_job(
        "Test Job",
        lambda: "DG AI Running",
        "10:00"
    )


    print(
        scheduler.get_jobs()
    )
