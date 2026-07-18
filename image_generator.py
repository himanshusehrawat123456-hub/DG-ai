"""
DG AI Version 1
Image Generator

Purpose:
- Manage AI image generation requests
- Create image generation records
- Store generated image information

Version: 1.0
"""

import logging
from datetime import datetime


class ImageGenerator:
    """
    Professional Image Generation System
    """

    def __init__(self):

        self.generated_images = []

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s"
        )


    # ---------------------------------

    def generate_image(
        self,
        prompt,
        style="default"
    ):
        """
        Generate image request.
        """

        record = {

            "id":
            len(self.generated_images) + 1,

            "prompt":
            prompt,

            "style":
            style,

            "image_file":
            f"generated_image_{len(self.generated_images)+1}.png",

            "status":
            "generated",

            "time":
            str(datetime.now())

        }


        self.generated_images.append(
            record
        )


        return record


    # ---------------------------------

    def add_style(
        self,
        style
    ):

        return True


    # ---------------------------------

    def get_generated_images(self):

        return self.generated_images


    # ---------------------------------

    def clear_images(self):

        self.generated_images.clear()

        return True



# ---------------------------------
# Testing
# ---------------------------------

if __name__ == "__main__":

    generator = ImageGenerator()


    print(
        generator.generate_image(
            "A futuristic AI robot"
        )
    )
