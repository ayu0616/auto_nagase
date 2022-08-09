from typing import Any
import chromedriver_binary  # noqa
from time import sleep
import requests
from nagase_driver import NagaseDriver


def get_token():
    driver = NagaseDriver()
    driver.login()
    nagase_token = driver.execute_script("return localStorage.getItem('CognitoIdentityServiceProvider.5c61idqvmdv797l9t913d1l1td.team169.idToken')")
    while not nagase_token:
        sleep(1)
        nagase_token = driver.execute_script("return localStorage.getItem('CognitoIdentityServiceProvider.5c61idqvmdv797l9t913d1l1td.team169.idToken')")
    driver.quit()
    return nagase_token


def get_tasks(token: str):
    headers = {
        "Authorization": f"Bearer {token}",
    }

    url = "https://production-apprunner-api.toshin-correction.com/sheets/assigned?"
    res = requests.get(url, headers=headers)
    tasks: dict[str, Any] = res.json()
    return tasks
