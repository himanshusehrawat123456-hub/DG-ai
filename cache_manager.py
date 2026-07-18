"""
DG AI Version 1
Cache Management System

Purpose:
- Manage temporary data storage
- Improve system performance
- Provide fast data access layer

Version: 1.0
"""


import time



class CacheManager:
    """
    Handles DG AI temporary memory cache.
    """



    def __init__(self):

        self.cache = {}



    def set_cache(self, key, value, expiry=None):
        """
        Store data in cache.

        Parameters:
            key: Cache name
            value: Data
            expiry: Time in seconds
        """

        self.cache[key] = {

            "value":
            value,

            "created":
            time.time(),

            "expiry":
            expiry

        }



    def get_cache(self, key):
        """
        Retrieve cache data.
        """

        if key not in self.cache:

            return None


        data = self.cache[key]


        if data["expiry"]:

            if time.time() - data["created"] > data["expiry"]:

                del self.cache[key]

                return None



        return data["value"]



    def remove_cache(self, key):
        """
        Remove cache item.
        """

        if key in self.cache:

            del self.cache[key]

            return True


        return False



    def clear_cache(self):
        """
        Clear complete cache.
        """

        self.cache.clear()

        return True



    def get_status(self):
        """
        Return cache information.
        """

        return {

            "items":
            len(self.cache),

            "status":
            "Active"

        }




# Testing

if __name__ == "__main__":


    cache = CacheManager()


    cache.set_cache(
        "user_name",
        "Himanshu"
    )


    print(
        cache.get_cache(
            "user_name"
        )
    )


    print(
        cache.get_status()
    )
