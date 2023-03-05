from flask import Flask, render_template

app = Flask(__name__, static_folder="static")
app.config["TRAP_HTTP_EXCEPTIONS"] = True


@app.errorhandler(Exception)
def error_handler(error):
    return render_template("error.html", error_code=error.code)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donate")
def donate():
    return render_template("donate.html")


if __name__ == '__main__':
    app.run(debug=True)
