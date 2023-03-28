import json
import yaml
from flask import render_template


class ConfigUtils:
    @classmethod
    def load_from_config(cls, config_filename: str, type_: str):
        with open(f"config/{config_filename}.json") as file:
            info = json.load(file)
        for block in info:
            if block["type"] == type_:
                return block["content"]

    @staticmethod
    def render_with_config(template_name: str, config_filename: str):
        with open(f"config/{config_filename}.yml") as stream:
            data = yaml.safe_load(stream)
        return render_template(template_name, data=data)
