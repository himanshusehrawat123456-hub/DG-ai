"""
DG AI Version 1
Data Validation System

Purpose:
- Validate user input
- Check data quality
- Provide safety foundation

Version: 1.0
"""


import re



class Validator:
    """
    Handles DG AI validation operations.
    """



    def __init__(self):

        self.errors = []



    def validate_text(self, text):
        """
        Validate text input.
        """

        if not text:

            self.errors.append(
                "Text cannot be empty"
            )

            return False


        if len(text.strip()) == 0:

            self.errors.append(
                "Invalid text"
            )

            return False


        return True



    def validate_email(self, email):
        """
        Validate email format.
        """

        pattern = (
            r'^[\w\.-]+@[\w\.-]+\.\w+$'
        )


        if re.match(pattern, email):

            return True


        self.errors.append(
            "Invalid email"
        )


        return False



    def validate_number(self, number):
        """
        Validate number input.
        """

        if isinstance(number, (int, float)):

            return True


        self.errors.append(
            "Invalid number"
        )


        return False



    def get_errors(self):
        """
        Return validation errors.
        """

        return self.errors



    def clear_errors(self):
        """
        Clear errors.
        """

        self.errors.clear()




# Testing

if __name__ == "__main__":


    validator = Validator()


    print(
        validator.validate_text(
            "Hello DG AI"
        )
    )


    print(
        validator.validate_email(
            "test@gmail.com"
        )
    )


    print(
        validator.get_errors()
    )
