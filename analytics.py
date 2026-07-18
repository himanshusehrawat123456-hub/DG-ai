# analytics.py
# DG AI Analytics System

import datetime


class Analytics:

    def __init__(self):
        self.logs = []


    def add_log(self, action):
        data = {
            "action": action,
            "time": str(datetime.datetime.now())
        }

        self.logs.append(data)
        print("Analytics Log Added:", data)


    def show_logs(self):

        print("\n--- DG AI Activity Logs ---")

        for log in self.logs:
            print(log)


    def total_actions(self):

        return len(self.logs)



# Testing

if __name__ == "__main__":

    ai_analytics = Analytics()

    ai_analytics.add_log("User opened DG AI")
    ai_analytics.add_log("User asked a question")
    ai_analytics.add_log("Voice command executed")

    ai_analytics.show_logs()

    print("Total Actions:",
          ai_analytics.total_actions())
