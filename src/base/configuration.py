import json
import os
import sys
import logging


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Configuration(metaclass=SingletonMeta):
    CONFIGURATION_JSON_FILE_NAME = "config.json"
    SRC_FOLDER_NAME = "src"
    ASSETS_FOLDER_NAME = "assets"

    settings = {}

    def __init__(self):
        assets_dir_path = (
            os.path.join(os.path.join(os.getcwd(), Configuration.ASSETS_FOLDER_NAME))
            if sys.platform == "emscripten"
            else os.path.join(
                os.getcwd(),
                Configuration.SRC_FOLDER_NAME,
                Configuration.ASSETS_FOLDER_NAME,
            )
        )

        with open(
            os.path.join(assets_dir_path, Configuration.CONFIGURATION_JSON_FILE_NAME)
        ) as config_file:
            config_json = json.load(config_file)
            for key in config_json:
                Configuration.settings[key] = config_json[key]
