import smtplib
import ssl
import os

email = "ahmed.elshabah2015@gmail.com"
passw = os.getenv("PASSWORD")
host = "smtp.gmail.com"
port = 465
context = ssl.create_default_context()


def send_gmail(message):
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(email, passw)
        server.sendmail(email, email, message)
