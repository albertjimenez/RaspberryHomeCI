from flask import jsonify
from flask import request

from .generate_app import generate_flask_app

# -*- coding: utf-8 -*-
# Flask APP
app = generate_flask_app(
    __name__)  # Initialize the app with your configurations e.g. app.config["SLACK_WEBHOOK"] = "....."


@app.route("/java/maven", methods=["POST"])
def java_maven():
    print("Webhook MAVEN entered \n{0}".format(request))


@app.route("/npm", methods=["POST"])
def npm():
    print("Webhook NPM entered \n{0}".format(request))
    return jsonify([1, 2, 3])


@app.route("/", methods=["GET"])
def test():
    print("Webhook NPM entered \n{0}".format(request))
    return jsonify([1])


@app.route("/", methods=["POST"])
def test_post():
    print("Webhook NPM POST entered \n{0}".format(request))
    return jsonify([1])


class HandlerTest:
    def __init__(self):
        pass

    def handle_java_maven(self, func: "function"):
        pass

    def handle_npm(self, func: "function"):
        pass


# TODO Runs the tests and receives the INT signal of the process, if SIGNAL > 0 error, else OK
import requests


# Sends the output of the test or an OK message through slack API
class SlackSender:
    def __init__(self, slack_url: "str"):
        self.slack_url = slack_url

    def send_msg(self, msg: "str"):
        r = requests.post(self.slack_url, json={"text": msg})
        if r.status_code != 200:
            # TODO log the errors
            print("Error sending MSG to Slack")


# Main
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
