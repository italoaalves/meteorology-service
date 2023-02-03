import smtplib
from settings import MAILER

class Mailer:
    def __init__(self, sender, receiver)
        self.smt_client = smtplib.SMTP('smtp.gmail.com', 587).starttls()
        self.smt_client.login()

     def __del__(self):
        self.smt_client.quit()

    def send_email(subject, message)
        body = f'Subject: {subject}\n\n{message}'
        self.smt_client.sendmail(MAILER['SENDER'], MAILER['RECEIVER'], body)
