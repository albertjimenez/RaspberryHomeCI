from sys import argv

from flask import jsonify, Flask
from flask import request
from slack_sender import SlackSender

# -*- coding: utf-8 -*-

# Check if the SLACK_WEBHOOK L it exists
SLACK_WEBHOOK = ""
if len(argv) != 2:
    print("Error, argument SLACK_WEBHOOK not present in execution. Usage: python3 main.py SLACK_WEBHOOK_URL_STRING")
    exit(1)
else:
    SLACK_WEBHOOK = argv[1]


# Flask APP
app = Flask(__name__)

slack_sender = SlackSender(SLACK_WEBHOOK)


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
