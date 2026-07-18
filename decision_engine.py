"""
DG AI Version 1
Decision Engine System

Purpose:
- Handle basic decisions
- Analyze conditions
- Provide reasoning foundation

Version: 1.0
"""


class DecisionEngine:
    """
    Handles DG AI decision operations.
    """



    def __init__(self):

        self.rules = []



    def add_rule(self, condition, action):
        """
        Add a decision rule.
        """

        rule = {

            "condition":
            condition,

            "action":
            action

        }


        self.rules.append(rule)


        return True



    def make_decision(self, input_data):
        """
        Make decision based on rules.
        """

        for rule in self.rules:

            if rule["condition"] in input_data:

                return rule["action"]


        return "No decision available"



    def get_rules(self):
        """
        Return all rules.
        """

        return self.rules




# Testing

if __name__ == "__main__":


    engine = DecisionEngine()


    engine.add_rule(
        "hello",
        "Respond with greeting"
    )


    engine.add_rule(
        "weather",
        "Provide weather information"
    )


    print(
        engine.make_decision(
            "hello DG AI"
        )
    )


    print(
        engine.get_rules()
    )
