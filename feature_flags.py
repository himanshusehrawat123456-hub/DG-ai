"""
DG AI Version 1
Feature Flags System

Purpose:
- Enable or disable AI features

Version: 1.0
"""


class FeatureFlags:
    """
    Handles feature control.
    """



    def __init__(self):

        self.features = {}



    def add_feature(self, name, status=False):
        """
        Add new feature.
        """

        self.features[name] = status

        return True



    def enable_feature(self, name):
        """
        Enable feature.
        """

        if name in self.features:

            self.features[name] = True

            return True


        return False



    def disable_feature(self, name):
        """
        Disable feature.
        """

        if name in self.features:

            self.features[name] = False

            return True


        return False



    def get_features(self):
        """
        Return all features.
        """

        return self.features




# Testing

if __name__ == "__main__":


    flags = FeatureFlags()


    flags.add_feature(
        "Voice AI"
    )


    flags.enable_feature(
        "Voice AI"
    )


    print(
        flags.get_features()
    )
