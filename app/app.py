from flask import Flask, render_template
import os
import argparse

import settings
from utils.config_utils import ConfigUtils

app = Flask(__name__, static_folder=settings.STATIC_FOLDER)
app.config["TRAP_HTTP_EXCEPTIONS"] = True


@app.errorhandler(Exception)
def error_handler(error):
    if hasattr(error, "code"):
        return render_template("error.j2", error_code=error.code)
    return render_template("error.j2", error_code=error)


@app.route("/")
def index():
    files = sorted(
        "/" + os.path.join(settings.SCREENSHOTS_FOLDER, file)
        for file in os.listdir(settings.SCREENSHOTS_FOLDER)
        if file.endswith(".png")
    )
    return render_template("index.j2", screenshots=files)


@app.route("/wiki")
def wiki():
    return ConfigUtils.render_with_config("wiki.j2", "wiki")


@app.route("/donate")
def donate():
    return render_template("donate.j2")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()
    settings.DEBUG = args.debug
    app.run(debug=settings.DEBUG, port=settings.PORT, host='0.0.0.0')
