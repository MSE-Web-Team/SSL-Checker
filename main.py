from CertChecker import CertChecker
from implemented.SSLCertReader import SSLCertReader
from implemented.MSEWebMailer import MSEWebMailer
from implemented.NotifierList import NotifierList
from implemented.SlackNotifier import SlackNotifier
from dotenv import load_dotenv
import os

load_dotenv()

hostnames = os.getenv("HOSTS").split(',')

notifierList = NotifierList([
    MSEWebMailer(
        smtp_hostname=os.getenv("SMTP_HOST"),
        sender=os.getenv("SMTP_SENDER"),
        notified=os.getenv("SMTP_SENDTO")
    ),
    SlackNotifier(
        token=os.getenv("SLACK_TOKEN"), 
        channel_id=os.getenv("SLACK_CHANNEL")
    )
])

CertChecker(notifierList, SSLCertReader()).checkHostnames(hostnames)
