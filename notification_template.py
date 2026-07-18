"""
DG AI Version 1
Notification Template

Purpose:
- Create notification templates
- Manage reusable messages
- Customize notification formats

Version: 1.0
"""

import logging
from datetime import datetime


class NotificationTemplate:
    """
    Professional Notification Template Manager
    """

    def __init__(self):

        self.templates = {}

        self.history = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def create_template(
        self,
        name,
        title,
        message
    ):
        """
        Create notification template.
        """

        template = {

            "name": name,

            "title": title,

            "message": message,

            "created":
            str(datetime.now())

        }


        self.templates[name] = template


        self.log_action(
            name,
            "created"
        )


        return template


    # ---------------------------------

    def get_template(
        self,
        name
    ):
        """
        Get template by name.
        """

        return self.templates.get(
            name
        )


    # ---------------------------------

    def update_template(
        self,
        name,
        title=None,
        message=None
    ):
        """
        Update existing template.
        """

        if name not in self.templates:

            return False


        if title:

            self.templates[name]["title"] = title


        if message:

            self.templates[name]["message"] = message


        self.log_action(
            name,
            "updated"
        )


        return True


    # ---------------------------------

    def delete_template(
        self,
        name
    ):
        """
        Delete template.
        """

        if name in self.templates:

            del self.templates[name]

            self.log_action(
                name,
                "deleted"
            )

            return True


        return False


    # ---------------------------------

    def render_template(
        self,
        name,
        data=None
    ):
        """
        Generate final notification message.
        """

        template = self.get_template(
            name
        )


        if not template:

            return None


        message = template["message"]


        if data:

            for key, value in data.items():

                message = message.replace(
                    "{" + key + "}",
                    str(value)
                )


        return {

            "title": template["title"],

            "message": message

        }


    # ---------------------------------

    def log_action(
        self,
        name,
        action
    ):

        self.history.append({

            "template": name,

            "action": action,

            "time": str(datetime.now())

        })


    # ---------------------------------

    def get_history(self):

        return self.history



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    template = NotificationTemplate()


    template.create_template(
        "welcome",
        "Welcome",
        "Hello {user}, DG AI Started"
    )


    print(
        template.render_template(
            "welcome",
            {
                "user": "Himanshu"
            }
        )
    )
