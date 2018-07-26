from sys import argv

from flask import jsonify, Flask
from flask import request
from handler import HandlerTest
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
handler_test = HandlerTest(slack_sender)


@app.route("/java/maven", methods=["POST"])
def java_maven():
    repository_details = request.get_json()["repository"]
    full_name, clone_url = repository_details["full_name"], repository_details["clone_url"]
    handler_test.handle_java_maven(full_name, clone_url)
    return jsonify(repository_details)


@app.route("/npm", methods=["POST"])
def npm():
    print("Webhook NPM entered \n{0}".format(request))
    repository_details = request.get_json()["repository"]
    slack_sender.send_msg("Test from python")
    full_name, clone_url = repository_details["full_name"], repository_details["clone_url"]
    handler_test.handle_npm(full_name, clone_url)
    return jsonify(repository_details)


# Main
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
