"""
DG AI - Browser Module
Version: 1.0
"""

import webbrowser
import logging
from datetime import datetime


class BrowserManager:

    def __init__(self):
        self.history = []

    def open_url(self, url):
        try:
            webbrowser.open(url)
            self.history.append(url)
            logging.info(f"Opened: {url}")
        except Exception as e:
            logging.error(e)

    def google(self):
        self.open_url("https://www.google.com")

    def youtube(self):
        self.open_url("https://www.youtube.com")

    def github(self):
        self.open_url("https://github.com")

    def show_history(self):
        print("\n===== Browser History =====")
        if not self.history:
            print("No history available.")
            return

        for i, url in enumerate(self.history, 1):
            print(f"{i}. {url}")

    def status(self):
        print("\nDG AI Browser Ready")
        print("Time:", datetime.now())


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    browser = BrowserManager()

    browser.google()
    browser.youtube()

    browser.show_history()
    browser.status()
