"""
DG AI Version 1
Memory Cache System

Purpose:
- Store temporary data in memory
- Retrieve and clear cached data

Version: 1.0
"""


import datetime


class MemoryCache:
    """
    Handles memory cache operations.
    """


    def __init__(self):

        self.cache = {}



    def set(self, key, value):
        """
        Store data in memory cache.
        """

        self.cache[key] = {

            "value": value,

            "time": str(datetime.datetime.now())

        }

        return True



    def get(self, key):
        """
        Get cached data.
        """

        if key in self.cache:

            return self.cache[key]["value"]

        return None



    def delete(self, key):
        """
        Delete cached data.
        """

        if key in self.cache:

            del self.cache[key]

            return True

        return False



    def clear(self):
        """
        Clear all cache.
        """

        self.cache.clear()

        return True



# Testing

if __name__ == "__main__":

    cache = MemoryCache()

    cache.set("username", "Himanshu")

    print(cache.get("username"))
