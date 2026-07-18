"""
DG AI - Plugin Manager
Version: 1.0
"""

import os
import logging


class PluginManager:

    def __init__(self):
        self.plugin_folder = "plugins"
        self.loaded_plugins = []

    def scan_plugins(self):
        print("Scanning plugins...")
        if os.path.exists(self.plugin_folder):
            files = os.listdir(self.plugin_folder)
            return files
        return []

    def load_plugin(self, plugin_name):
        if plugin_name not in self.loaded_plugins:
            self.loaded_plugins.append(plugin_name)
            logging.info(f"Loaded Plugin: {plugin_name}")

    def unload_plugin(self, plugin_name):
        if plugin_name in self.loaded_plugins:
            self.loaded_plugins.remove(plugin_name)
            logging.info(f"Unloaded Plugin: {plugin_name}")

    def list_plugins(self):
        print("\n===== Loaded Plugins =====")
        if not self.loaded_plugins:
            print("No plugins loaded.")
            return

        for plugin in self.loaded_plugins:
            print(plugin)

    def status(self):
        print("DG AI Plugin Manager Ready")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    manager = PluginManager()

    manager.load_plugin("Chat")
    manager.load_plugin("Voice")

    manager.list_plugins()

    manager.status()
