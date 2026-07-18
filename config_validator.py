"""
DG AI Version 1
Configuration Validator

Purpose:
- Validate configuration data
- Check required configuration fields

Version: 1.0
"""


class ConfigValidator:
    """
    Handles configuration validation.
    """

    def __init__(self):

        self.required_keys = [
            "app_name",
            "version"
        ]


    def validate(self, config_data):
        """
        Validate configuration.
        """

        missing_keys = []

        for key in self.required_keys:

            if key not in config_data:

                missing_keys.append(key)

        return {
            "valid": len(missing_keys) == 0,
            "missing_keys": missing_keys
        }


# Testing

if __name__ == "__main__":

    validator = ConfigValidator()

    sample_config = {
        "app_name": "DG AI",
        "version": "1.0.0"
    }

    print(
        validator.validate(
            sample_config
        )
    )
