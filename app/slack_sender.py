import requests
from ISender import ISender


# Sends the output of the test or an OK message through slack API
class SlackSender(ISender):
    def __init__(self, slack_url):
        self.slack_url = slack_url

    def send_msg(self, msg):
        r = requests.post(self.slack_url, json={"text": msg})
        if r.status_code != 200:
            # TODO log the errors
            print("Error sending MSG to Slack")
        else:
            print("Message sent successfully")
