import smtplib
import email.message
from os import getenv


class Mailer:
    def __init__(self):
        self.smtp_client = smtplib.SMTP('smtp.gmail.com', 587)
        self.smtp_client.starttls()
        self.smtp_client.login(getenv('SENDER_EMAIL'), getenv('SMTP_PASSWORD'))

    def send_email(self, subject, body):
        message = email.message.Message()
        message['Subject'] = subject
        message['From'] = getenv('SENDER_EMAIL')
        message['To'] = getenv('RECEIVER_EMAIL')
        message.add_header('Content-Type', 'text/html')
        message.set_payload(body)

        self.smtp_client.sendmail(message['From'], message['To'], message.as_string().encode('utf-8'))

    def __del__(self):
        self.smtp_client.quit()
