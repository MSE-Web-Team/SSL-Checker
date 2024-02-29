from interface.Notifier import Notifier
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class MSEWebMailer(Notifier):

    def __init__(self, smtp_hostname, sender, notified, smtp_port=25, smtp_username="", smtp_password=""):
        self.smtp_hostname = smtp_hostname
        self.smtp_port = smtp_port
        self.sender = sender
        self.notified = notified
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password

    def notify(self, hostname, day):

        body = f"""
            The SSL certificate for {hostname} is expiring on {day}. 
            Please renew the certificate as soon as possible.
        """

        message = MIMEMultipart()
        message["From"] = self.sender
        message["To"] = self.notified
        message["subject"] = f"SSL certificate for {hostname} expiring soon"
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(self.smtp_hostname, self.smtp_port) as server:
            #server.set_debuglevel(1)
            text = message.as_string()
            server.sendmail(self.sender, self.notified, text)
