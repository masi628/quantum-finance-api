import os
import ssl
import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, content):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = os.environ.get("SMTP_USER")
    msg["To"] = to_email
    msg.set_content(content)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(os.environ.get("SMTP_HOST"), int(os.environ.get("SMTP_PORT")), context=context) as server:
        server.login(os.environ.get("SMTP_USER"), os.environ.get("SMTP_PASS"))
        server.send_message(msg)
