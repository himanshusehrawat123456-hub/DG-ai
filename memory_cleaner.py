"""
DG AI Version 1
Memory Cleaner

Purpose:
- Clean old AI memories
- Remove unwanted records
- Maintain memory quality

Version: 1.0
"""

import logging
from datetime import datetime, timedelta


class MemoryCleaner:
    """
    Professional AI Memory Cleaner
    """

    def __init__(self):

        self.clean_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def remove_empty_memory(
        self,
        memories
    ):
        """
        Remove empty memory records.
        """

        cleaned = []


        for memory in memories:

            if memory.get("information"):

                cleaned.append(memory)


        self.log_cleaning(
            "Empty memory removed"
        )


        return cleaned


    # ---------------------------------

    def remove_duplicate_memory(
        self,
        memories
    ):
        """
        Remove duplicate memories.
        """

        unique = []

        seen = set()


        for memory in memories:

            info = str(
                memory.get("information")
            )


            if info not in seen:

                seen.add(info)

                unique.append(memory)


        self.log_cleaning(
            "Duplicate memory removed"
        )


        return unique


    # ---------------------------------

    def clean_old_memory(
        self,
        memories,
        days=30
    ):
        """
        Remove old memory records.
        """

        valid_memory = []

        limit = datetime.now() - timedelta(
            days=days
        )


        for memory in memories:

            try:

                created = datetime.fromisoformat(
                    memory["created"]
                )


                if created >= limit:

                    valid_memory.append(
                        memory
                    )


            except Exception:

                valid_memory.append(
                    memory
                )


        self.log_cleaning(
            "Old memory cleaned"
        )


        return valid_memory


    # ---------------------------------

    def optimize_memory(
        self,
        memories
    ):
        """
        Run complete cleaning process.
        """

        result = self.remove_empty_memory(
            memories
        )


        result = self.remove_duplicate_memory(
            result
        )


        return result


    # ---------------------------------

    def log_cleaning(
        self,
        action
    ):

        self.clean_history.append({

            "action": action,

            "time": str(datetime.now())

        })


    # ---------------------------------

    def get_history(self):

        return self.clean_history


    # ---------------------------------

    def clear_history(self):

        self.clean_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    cleaner = MemoryCleaner()


    sample = [

        {
            "information": "DG AI",
            "created": str(datetime.now())
        },

        {
            "information": "",
            "created": str(datetime.now())
        }

    ]


    print(
        cleaner.optimize_memory(
            sample
        )
    )
