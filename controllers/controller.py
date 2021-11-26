from flask import render_template
from app import app


@app.route("/")
def home():
    return render_template("base.html", title="test")


# @app.route("/events", methods=["POST"])
# def add_event():
#     return "Some String"
