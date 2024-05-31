import json

def load_settings(file_path):
    with open(file_path, 'r') as f:
        settings = json.load(f)
    return settings

def get_setting(settings, key):
    return settings.get(key)