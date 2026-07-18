"""
DG AI Version 1
Image Manager System

Purpose:
- Manage image operations
- Store image information

Version: 1.0
"""


import datetime



class ImageManager:
    """
    Handles image management.
    """



    def __init__(self):

        self.images = []



    def add_image(self, name, path):
        """
        Add image record.
        """

        image = {

            "id":
            len(self.images) + 1,

            "name":
            name,

            "path":
            path,

            "time":
            str(datetime.datetime.now())

        }


        self.images.append(image)


        return image



    def get_images(self):
        """
        Return images list.
        """

        return self.images



    def remove_image(self, image_id):
        """
        Remove image record.
        """

        for image in self.images:

            if image["id"] == image_id:

                self.images.remove(image)

                return True


        return False




# Testing

if __name__ == "__main__":


    manager = ImageManager()


    print(
        manager.add_image(
            "test.png",
            "/images/test.png"
        )
    )
