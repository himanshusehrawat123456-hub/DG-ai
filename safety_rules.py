"""
DG AI Version 1
Safety Rules System

Purpose:
- Manage AI safety rules
- Control AI behavior guidelines

Version: 1.0
"""


import datetime



class SafetyRules:
    """
    Handles AI safety rules.
    """



    def __init__(self):

        self.rules = []

        self.history = []



    def add_rule(self, rule):
        """
        Add new safety rule.
        """

        data = {

            "id":
            len(self.rules) + 1,

            "rule":
            rule,

            "time":
            str(datetime.datetime.now())

        }


        self.rules.append(data)


        return True



    def get_rules(self):
        """
        Return all safety rules.
        """

        return self.rules



    def remove_rule(self, rule_id):
        """
        Remove safety rule.
        """

        for rule in self.rules:

            if rule["id"] == rule_id:

                self.rules.remove(rule)

                return True


        return False



    def check_rule_exists(self, text):
        """
        Check if text matches any rule.
        """

        for rule in self.rules:

            if rule["rule"].lower() in text.lower():

                return True


        return False




# Testing

if __name__ == "__main__":


    safety = SafetyRules()


    safety.add_rule(
        "Respect user privacy"
    )


    print(
        safety.get_rules()
    )
