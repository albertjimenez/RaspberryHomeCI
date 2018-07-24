from flask import jsonify
from flask import request
from generate_app import generate_flask_app

from utils.slack_sender import SlackSender

# -*- coding: utf-8 -*-
# Flask APP
app = generate_flask_app(
    __name__)  # Initialize the app with your configurations e.g. app.config["SLACK_WEBHOOK"] = "....."

slack_sender = SlackSender(app.config["SLACK_WEBHOOK"])


@app.route("/java/maven", methods=["POST"])
def java_maven():
    print("Webhook MAVEN entered \n{0}".format(request))
    slack_sender.send_msg("Test from python")
    return jsonify([1])


@app.route("/npm", methods=["POST"])
def npm():
    print("Webhook NPM entered \n{0}".format(request))
    slack_sender.send_msg("Test from python")
    return jsonify([1, 2, 3])


@app.route("/", methods=["GET"])
def test():
    print("Webhook NPM entered \n{0}".format(request))
    slack_sender.send_msg("Test from python")
    return jsonify([1])


@app.route("/", methods=["POST"])
def test_post():
    print("Webhook NPM POST entered \n{0}".format(request))
    return jsonify([1])


# Main
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
