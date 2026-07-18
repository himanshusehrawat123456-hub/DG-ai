"""
DG AI Version 1
Plugin Registry System

Purpose:
- Register plugins
- Manage plugin information

Version: 1.0
"""


import datetime



class PluginRegistry:
    """
    Handles plugin registration.
    """



    def __init__(self):

        self.plugins = []



    def register_plugin(self, name, version, description):
        """
        Register a new plugin.
        """

        plugin = {

            "id":
            len(self.plugins) + 1,

            "name":
            name,

            "version":
            version,

            "description":
            description,

            "status":
            "active",

            "time":
            str(datetime.datetime.now())

        }


        self.plugins.append(plugin)


        return True



    def get_plugins(self):
        """
        Return all plugins.
        """

        return self.plugins



    def find_plugin(self, name):
        """
        Find plugin by name.
        """

        for plugin in self.plugins:

            if plugin["name"] == name:

                return plugin


        return None



    def remove_plugin(self, name):
        """
        Remove plugin.
        """

        for plugin in self.plugins:

            if plugin["name"] == name:

                self.plugins.remove(plugin)

                return True


        return False




# Testing

if __name__ == "__main__":


    registry = PluginRegistry()


    registry.register_plugin(
        "Calculator",
        "1.0",
        "Math calculation tool"
    )


    print(
        registry.get_plugins()
    )
