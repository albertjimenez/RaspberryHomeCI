import os
from sys import argv

from Services import space
from flask import jsonify, Flask
from flask import request
from handler import HandlerTest
from psutil import cpu_percent
from slack_sender import SlackSender

# -*- coding: utf-8 -*-

# Check if the SLACK_WEBHOOK exists as environmental variable or as an argument
SLACK_WEBHOOK = os.getenv('SLACK_WEBHOOK', "1")
if SLACK_WEBHOOK == "1" and len(argv) != 2:
    print("Error, argument SLACK_WEBHOOK not present in execution or as an enviornmental variable. "
          "Usage: python3 main.py SLACK_WEBHOOK_URL_STRING")
    exit(1)
else:
    if SLACK_WEBHOOK == "1":
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


@app.route("/api/hdd_info")
def get_space():
    free_space, total = space()
    res_space = {
        "free_space": free_space,
        "total": total
    }
    return jsonify(res_space)


@app.route("/api/cpu_info")
def cpu_info():
    return jsonify({"cpu": cpu_percent()})


# Main
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
