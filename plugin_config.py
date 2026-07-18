"""
DG AI Version 1
Plugin Configuration System

Purpose:
- Manage plugin settings
- Store plugin configuration

Version: 1.0
"""


import datetime



class PluginConfig:
    """
    Handles plugin configuration.
    """



    def __init__(self):

        self.configurations = {}



    def add_config(self, plugin_name, settings):
        """
        Add plugin configuration.
        """

        self.configurations[plugin_name] = {

            "settings":
            settings,

            "created":
            str(datetime.datetime.now())

        }


        return True



    def update_config(self, plugin_name, settings):
        """
        Update plugin configuration.
        """

        if plugin_name in self.configurations:

            self.configurations[plugin_name]["settings"] = settings

            return True


        return False



    def get_config(self, plugin_name):
        """
        Get plugin configuration.
        """

        return self.configurations.get(plugin_name)



    def get_all_configs(self):
        """
        Return all configurations.
        """

        return self.configurations




# Testing

if __name__ == "__main__":


    config = PluginConfig()


    config.add_config(
        "Calculator Tool",
        {
            "enabled": True,
            "version": "1.0"
        }
    )


    print(
        config.get_all_configs()
    )
