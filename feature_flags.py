import json

class FeatureFlags:
    def __init__(self, config_file = "feature_flags.json"):
        self.config_file = config_file
        self.flags = self.load_flags()

    def load_flags(self):
        try:
            with open(self.config_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def is_enabled(self, feature_name):
        return self.flags.get(feature_name, False)

    def enable(self, feature_name):
        self.flags[feature_name] = True
        self.save_flags()

    def disable(self, feature_name):
        self.flags[feature_name] = False
        self.save_flags()

    def save_flags(self):
        with open(self.config_file, "w") as file:
            json.dump(self.flags, file, indent = 4)
