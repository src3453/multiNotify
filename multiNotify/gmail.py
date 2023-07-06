import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

GMAIL_URL = "smtp.gmail.com"
GMAIL_PORT = 465

class gmail:
    def __init__(self,app_password) -> None:
        self.password=app_password
    def send_email(self,sender_email="", receiver_email="", text="", html="", subject=""):
        
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = receiver_email

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(GMAIL_URL, GMAIL_PORT, context=context) as server:
            server.login(sender_email, self.password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )