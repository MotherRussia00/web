import json
import yaml
from flask import render_template
import settings


class ConfigUtils:
    cached = dict()

    @classmethod
    def load_from_config(cls, config_filename: str, type_: str):
        with open(f"config/{config_filename}.json", encoding="utf-8") as file:
            info = json.load(file)
        for block in info:
            if block["type"] == type_:
                return block["content"]
    
    @classmethod
    def render_with_config(cls, template_name: str, config_filename: str):
        file = f"config/{config_filename}.yml"
        if settings.DEBUG or file not in cls.cached:
            with open(file, 'r', encoding="utf-8") as stream:
                cls.cached[file] = yaml.safe_load(stream)
        return render_template(template_name, data=cls.cached[file])
