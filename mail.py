from email.mime.text import MIMEText
from email.utils import formatdate
import smtplib
from settings import GMAIL_ADDRESS, ICLOUD_ADDRESS


class Mail(smtplib.SMTP):
    def __init__(self, host: str, port: int) -> None:
        super().__init__(host=host, port=port)

    def login(self, user: str, password: str, *, initial_response_ok=True) -> tuple[int, bytes]:
        self.ehlo()
        self.starttls()
        self.ehlo()
        return super().login(user, password, initial_response_ok=initial_response_ok)


class MailText(MIMEText):
    def __init__(self, _text: str) -> None:
        super().__init__(_text)
        self["Subject"] = "採点業務がまだ終了していません"
        self["from"] = GMAIL_ADDRESS
        self["to"] = ICLOUD_ADDRESS
        self["Date"] = formatdate()
