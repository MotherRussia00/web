from flask import Flask, render_template
import os

app = Flask(__name__, static_folder="static")
app.config["TRAP_HTTP_EXCEPTIONS"] = True

@app.errorhandler(Exception)
def error_handler(error):
    return render_template("error.html", error_code=error.code)


@app.route("/")
def index():
    screenshots_folder = "static/img/screenshots/"
    files = os.listdir(screenshots_folder)
    filter(lambda f: f.endswith(".png"), files)
    files = [ "/" + os.path.join(screenshots_folder, f) for f in files ]
    files.sort()
    return render_template("index.html", screenshots=files)


@app.route("/donate")
def donate():
    return render_template("donate.html")


if __name__ == '__main__':
    app.run(debug=True)
