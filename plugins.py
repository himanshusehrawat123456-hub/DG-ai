"""
DG AI - Plugin System
Version: 1.0
"""

import logging


class Plugin:
    def __init__(self, name, version="1.0"):
        self.name = name
        self.version = version
        self.enabled = False

    def enable(self):
        self.enabled = True
        logging.info(f"{self.name} Enabled")

    def disable(self):
        self.enabled = False
        logging.info(f"{self.name} Disabled")

    def status(self):
        state = "Enabled" if self.enabled else "Disabled"
        print(f"{self.name} ({self.version}) : {state}")


class PluginManager:
    def __init__(self):
        self.plugins = {}

    def register(self, plugin):
        self.plugins[plugin.name] = plugin
        logging.info(f"Plugin Registered: {plugin.name}")

    def remove(self, name):
        if name in self.plugins:
            del self.plugins[name]
            logging.info(f"Plugin Removed: {name}")

    def enable(self, name):
        if name in self.plugins:
            self.plugins[name].enable()

    def disable(self, name):
        if name in self.plugins:
            self.plugins[name].disable()

    def list_plugins(self):
        print("\n===== DG AI Plugins =====")
        if not self.plugins:
            print("No plugins installed.")
            return

        for plugin in self.plugins.values():
            plugin.status()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    manager = PluginManager()

    p1 = Plugin("Chat Plugin")
    p2 = Plugin("Voice Plugin")
    p3 = Plugin("Search Plugin")

    manager.register(p1)
    manager.register(p2)
    manager.register(p3)

    manager.enable("Chat Plugin")
    manager.enable("Voice Plugin")

    manager.list_plugins()
