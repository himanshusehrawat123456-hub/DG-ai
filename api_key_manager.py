"""
DG AI Version 1
API Key Management System

Purpose:
- Store and manage API keys
- Protect external service credentials
- Provide secure integration foundation

Version: 1.0
"""


import json
import os



class APIKeyManager:
    """
    Handles DG AI API key operations.
    """



    def __init__(self, file_path="data/api_keys.json"):

        self.file_path = file_path

        self.api_keys = {}

        self._create_storage()

        self._load_keys()



    def _create_storage(self):
        """
        Create storage folder.
        """

        folder = os.path.dirname(
            self.file_path
        )


        if folder and not os.path.exists(folder):

            os.makedirs(folder)



    def add_key(self, service, key):
        """
        Add new API key.
        """

        self.api_keys[service] = key

        self._save_keys()


        return True



    def get_key(self, service):
        """
        Retrieve API key.
        """

        return self.api_keys.get(
            service,
            None
        )



    def remove_key(self, service):
        """
        Remove API key.
        """

        if service in self.api_keys:

            del self.api_keys[service]

            self._save_keys()

            return True


        return False



    def list_services(self):
        """
        Return available services.
        """

        return list(
            self.api_keys.keys()
        )



    def _save_keys(self):
        """
        Save API keys.
        """

        with open(
            self.file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.api_keys,
                file,
                indent=4
            )



    def _load_keys(self):
        """
        Load saved API keys.
        """

        if os.path.exists(self.file_path):

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.api_keys = json.load(file)




# Testing

if __name__ == "__main__":


    manager = APIKeyManager()


    manager.add_key(
        "AI_Service",
        "YOUR_API_KEY"
    )


    print(
        "Available Services:"
    )


    print(
        manager.list_services()
    )
