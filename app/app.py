from flask import Flask, render_template, redirect
import os
import json
import argparse

import settings
from forms import DonateColorNicknameForm
from utils import PayUtils, ConfigUtils

app = Flask(__name__, static_folder=settings.STATIC_FOLDER)
app.config["TRAP_HTTP_EXCEPTIONS"] = True


@app.errorhandler(Exception)
def error_handler(error):
    if hasattr(error, "code"):
        return render_template("error.j2", error_code=error.code)
    return render_template("error.j2", error_code=error)


@app.route("/donate/nickname", methods=["POST", "GET"])
def nickname_donate():
    form = DonateColorNicknameForm()
    if form.validate_on_submit():
        info = PayUtils.create_pay_request(info={
            "type": "nickname",
            "color": form.color.data,
            "nickname": form.nickname.data
        })
        return redirect(info.base_url)
    return render_template("nickname_donate.html", form=form)


@app.route("/operation/<string:uuid>")
def operation(uuid: str):
    str_info, _ = uuid.split(":")
    info = json.load(str_info)

    if info["type"] == "nickname":
        pass


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
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    settings.DEBUG = args.debug
    app.run(debug=settings.DEBUG, port=settings.PORT, host="0.0.0.0")
