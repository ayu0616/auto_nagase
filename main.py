from get_tasks import get_tasks, get_token
from settings import GMAIL_ADDRESS, GMAIL_PASSWORD, ICLOUD_ADDRESS
from mail import Mail, MailText

nagase_token = get_token()
tasks = get_tasks(nagase_token)

if not tasks:
    exit()

is_finished = True
for task in tasks:
    is_finished = is_finished and task["uploaded"]

if is_finished:
    exit()

smtpobj = Mail("smtp.gmail.com", 587)
if type(GMAIL_ADDRESS) != str or type(GMAIL_PASSWORD) != str or type(ICLOUD_ADDRESS) != str:
    raise Exception("メールアドレスかパスワードが見つかりませんでした")
smtpobj.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
msg = MailText(str(tasks))
smtpobj.sendmail(GMAIL_ADDRESS, ICLOUD_ADDRESS, msg.as_string())
smtpobj.close()
