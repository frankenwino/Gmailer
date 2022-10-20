"""
Signing into Gmail with an app password:
    https://support.google.com/accounts/answer/185833

Rename configTEMPLATE.json to config.json
Add your Gmail information to config.json
"""
import smtplib
import json
from email.message import EmailMessage
import pathlib


def gmail_config() -> dict:
    """gmail_config handles the opening of a json file and converting its
    contents to a dictionary.

    Returns:
        dict: Gmail server and login credentials.
    """    
    json_file = pathlib.Path(__file__).parent.joinpath("config.json")
    with open(json_file) as f:
        gmail_cfg = json.load(f)

    return gmail_cfg


def send_email(recipient: str, subject: str, message: str):
    """send_email sends email via a Gmail account.

    Args:
        recipient (str): the recipient's email address.
        subject (str): the email subject.
        message (str): the body of the email.
    """
    gmail_cfg = gmail_config()
    msg = EmailMessage()
    msg["to"] = recipient
    msg["from"] = gmail_cfg["email"]
    msg["Subject"] = subject
    msg.set_content(message)

    # Create SMTP client, login to gmail and send the email
    with smtplib.SMTP_SSL(gmail_cfg["server"], gmail_cfg["port"]) as smtp:
        smtp.login(gmail_cfg["email"], gmail_cfg["app_pwd"])
        smtp.send_message(msg)
        print("Email sent!")
