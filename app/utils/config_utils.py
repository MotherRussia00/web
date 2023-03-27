import json


class ConfigUtils:
    @classmethod
    def load_from_config(cls, config_filename: str, type_: str):
        with open(f"json/{config_filename}.json") as file:
            info = json.load(file)
        for block in info:
            if block["type"] == type_:
                return block["content"]
