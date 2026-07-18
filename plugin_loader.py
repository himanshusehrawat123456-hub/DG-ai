"""
DG AI Version 1
Plugin Loader System

Purpose:
- Load and manage plugins
- Provide extension system foundation

Version: 1.0
"""


import datetime



class PluginLoader:
    """
    Handles DG AI plugin loading operations.
    """



    def __init__(self):

        self.plugins = []



    def register_plugin(self, name, module):
        """
        Register new plugin.
        """

        plugin = {

            "id":
            len(self.plugins) + 1,

            "name":
            name,

            "module":
            module,

            "status":
            "Loaded",

            "time":
            str(datetime.datetime.now())

        }


        self.plugins.append(plugin)


        return True



    def remove_plugin(self, plugin_id):
        """
        Remove plugin.
        """

        for plugin in self.plugins:

            if plugin["id"] == plugin_id:

                self.plugins.remove(plugin)

                return True


        return False



    def get_plugins(self):
        """
        Return all plugins.
        """

        return self.plugins



    def check_plugin(self, name):
        """
        Check plugin availability.
        """

        for plugin in self.plugins:

            if plugin["name"] == name:

                return plugin


        return None




# Testing

if __name__ == "__main__":


    loader = PluginLoader()


    loader.register_plugin(
        "Voice Plugin",
        "voice_manager"
    )


    print(
        loader.get_plugins()
    )
