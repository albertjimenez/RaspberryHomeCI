from flask import Flask


def generate_flask_app(class_name):
    app = Flask(class_name)
    app.config["SLACK_WEBHOOK"] = ""
    return app
