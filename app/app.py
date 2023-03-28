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
        return render_template("error.html", error_code=error.code)
    return render_template("error.html", error_code=error)


@app.route("/")
def index():
    files = sorted(
        "/" + os.path.join(settings.SCREENSHOTS_FOLDER, file)
        for file in os.listdir(settings.SCREENSHOTS_FOLDER)
        if file.endswith(".png")
    )
    return render_template("index.html", screenshots=files)


@app.route("/wiki")
def wiki():
    return ConfigUtils.render_with_config("wiki.html", "wiki")


@app.route("/donate")
def donate():
    return render_template("donate.html")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    app.run(debug=args.debug, port=settings.PORT, host='0.0.0.0')
