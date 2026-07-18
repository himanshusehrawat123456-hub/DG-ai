"""
DG AI Version 1
Response Generator System

Purpose:
- Generate AI responses
- Manage basic response patterns
- Provide reply generation foundation

Version: 1.0
"""


import random



class ResponseGenerator:
    """
    Handles DG AI response generation.
    """



    def __init__(self):

        self.responses = {

            "hello": [
                "Hello, I am DG AI.",
                "Hi, how can I help you?"
            ],

            "bye": [
                "Goodbye.",
                "See you again."
            ],

            "thanks": [
                "You are welcome.",
                "Happy to help."
            ]

        }



    def generate_response(self, user_input):
        """
        Generate response from input.
        """

        text = user_input.lower()


        for key in self.responses:

            if key in text:

                return random.choice(
                    self.responses[key]
                )


        return (
            "I am learning. "
            "Please provide more information."
        )



    def add_response(self, keyword, responses):
        """
        Add new response pattern.
        """

        self.responses[keyword] = responses


        return True



    def get_responses(self):
        """
        Return response database.
        """

        return self.responses




# Testing

if __name__ == "__main__":


    generator = ResponseGenerator()


    print(
        generator.generate_response(
            "Hello DG AI"
        )
    )


    print(
        generator.generate_response(
            "Thanks"
        )
    )
