"""
DG AI Version 1
Video Manager System

Purpose:
- Manage video files
- Store video information

Version: 1.0
"""


import datetime



class VideoManager:
    """
    Handles video management.
    """



    def __init__(self):

        self.videos = []



    def add_video(self, name, path):
        """
        Add video record.
        """

        video = {

            "id":
            len(self.videos) + 1,

            "name":
            name,

            "path":
            path,

            "time":
            str(datetime.datetime.now())

        }


        self.videos.append(video)


        return video



    def get_videos(self):
        """
        Return video list.
        """

        return self.videos



    def remove_video(self, video_id):
        """
        Remove video record.
        """

        for video in self.videos:

            if video["id"] == video_id:

                self.videos.remove(video)

                return True


        return False




# Testing

if __name__ == "__main__":


    manager = VideoManager()


    print(
        manager.add_video(
            "demo.mp4",
            "/videos/demo.mp4"
        )
    )
