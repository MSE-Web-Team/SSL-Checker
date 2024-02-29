from interface.Notifier import Notifier
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

class SlackNotifier(Notifier):
    def __init__(self, token, channel_id):
        self.channel_id = channel_id
        self.client = WebClient(token=token)

    def notify(self, hostname, day):
        message = f"""
            The SSL certificate for {hostname} is expiring on {day}. Please renew the certificate as soon as possible.
        """
        try:
            self.client.chat_postMessage(channel=self.channel_id, text=message)
        except SlackApiError as e:
            print(f"Error sending slack message: {e}")