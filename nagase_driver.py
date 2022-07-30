from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from settings import NAGASE_ID, NAGASE_PASSWORD


class NagaseDriver(webdriver.Chrome):
    def __init__(self):
        caps = DesiredCapabilities.CHROME
        caps["goog:loggingPrefs"] = {"performance": "ALL"}

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--ignore-certificate-errors")

        super().__init__(options=options, desired_capabilities=caps)

    def login(self):
        login_url = "https://www.toshin-correction.com/"
        self.get(login_url)
        self.find_element(By.ID, "uid").send_keys(NAGASE_ID)
        self.find_element(By.ID, "password").send_keys(NAGASE_PASSWORD)
        self.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
