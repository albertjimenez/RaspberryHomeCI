# TODO Runs the tests and receives the INT signal of the process, if SIGNAL > 0 error, else OK
from _thread import start_new_thread as new_thread

import requests


# Sends the output of the test or an OK message through slack API
class SlackSender:
    def __init__(self, slack_url):
        self.slack_url = slack_url

    def send_msg(self, msg):
        def f(url, m):
            r = requests.post(url, json={"text": m})
            if r.status_code != 200:
                # TODO log the errors
                print("Error sending MSG to Slack")

        new_thread(f, (self.slack_url, msg,))
