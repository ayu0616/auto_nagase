import chromedriver_binary  # noqa
from time import sleep
import requests
from mail import Mail, MailText
from nagase_driver import NagaseDriver
from settings import GMAIL_ADDRESS, GMAIL_PASSWORD, ICLOUD_ADDRESS

driver = NagaseDriver()
driver.login()
nagase_token = driver.execute_script("return localStorage.getItem('CognitoIdentityServiceProvider.5c61idqvmdv797l9t913d1l1td.team169.idToken')")
while not nagase_token:
    sleep(1)
    nagase_token = driver.execute_script("return localStorage.getItem('CognitoIdentityServiceProvider.5c61idqvmdv797l9t913d1l1td.team169.idToken')")
driver.quit()

headers = {
    "Authorization": f"Bearer {nagase_token}",
}

url = "https://production-apprunner-api.toshin-correction.com/sheets/assigned?"
res = requests.get(url, headers=headers)
tasks = res.json()

if tasks:
    smtpobj = Mail("smtp.gmail.com", 587)
    if type(GMAIL_ADDRESS) != str or type(GMAIL_PASSWORD) != str or type(ICLOUD_ADDRESS) != str:
        raise Exception("メールアドレスかパスワードが見つかりませんでした")
    smtpobj.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
    msg = MailText(str(tasks))
    smtpobj.sendmail(GMAIL_ADDRESS, ICLOUD_ADDRESS, msg.as_string())
    smtpobj.close()
