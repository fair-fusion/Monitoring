import json

class Config:
    def __init__(self, config_file="config/settings.json"):
        with open(config_file) as f:
            self.settings = json.load(f)

    @property
    def threshold(self):
        return self.settings["threshold"]

    @property
    def email_settings(self):
        return self.settings["email"]

    @property
    def fixed_values(self):
        return self.settings["fixed_values"]

    @property
    def batch_number(self):
        return self.settings["batch_number"]