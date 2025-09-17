from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("open-source.html")


@app.route("/pdf")
def home_pdf():
    return send_from_directory(
        directory=os.path.join(app.root_path, "templates"), path="open-source.pdf"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1234)
