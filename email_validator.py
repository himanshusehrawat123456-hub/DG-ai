"""
DG AI Version 1
Email Validator

Purpose:
- Validate email addresses
- Check email data format
- Provide validation reports

Version: 1.0
"""

import re
import logging
from datetime import datetime


class EmailValidator:
    """
    Professional Email Validation Manager
    """

    def __init__(self):

        self.validation_history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def validate_address(
        self,
        email
    ):
        """
        Validate email address format.
        """

        pattern = (
            r'^[\w\.-]+@[\w\.-]+\.\w+$'
        )


        result = bool(
            re.match(
                pattern,
                email
            )
        )


        return result


    # ---------------------------------

    def check_required_fields(
        self,
        data
    ):
        """
        Check required email fields.
        """

        required = [

            "receiver",

            "subject",

            "message"

        ]


        missing = []


        for field in required:

            if field not in data:

                missing.append(field)


        return {

            "valid":
            len(missing) == 0,

            "missing":
            missing

        }


    # ---------------------------------

    def validate_email(
        self,
        data
    ):
        """
        Complete email validation.
        """

        result = {

            "valid": True,

            "errors": []

        }


        if "receiver" not in data:

            result["valid"] = False

            result["errors"].append(
                "Receiver missing"
            )


        else:

            if not self.validate_address(
                data["receiver"]
            ):

                result["valid"] = False

                result["errors"].append(
                    "Invalid email address"
                )


        fields = self.check_required_fields(
            data
        )


        if not fields["valid"]:

            result["valid"] = False

            result["errors"].extend(
                fields["missing"]
            )


        record = {

            "data": data,

            "result": result,

            "time": str(datetime.now())

        }


        self.validation_history.append(
            record
        )


        logging.info(
            "Email validation completed"
        )


        return record


    # ---------------------------------

    def get_history(self):

        return self.validation_history


    # ---------------------------------

    def clear_history(self):

        self.validation_history.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    validator = EmailValidator()


    sample = {

        "receiver":
        "test@example.com",

        "subject":
        "Test",

        "message":
        "Hello"

    }


    print(
        validator.validate_email(
            sample
        )
    )
