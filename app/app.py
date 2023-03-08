from flask import Flask, render_template
import os

import settings

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


@app.route("/donate")
def donate():
    return render_template("donate.html")


if __name__ == '__main__':
    app.run(debug=settings.DEBUG, port=settings.PORT, host='0.0.0.0')
