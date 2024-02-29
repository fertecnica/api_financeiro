from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BankScrapper:
    def __init__(self, web_navigator):
        self.web_navigator = web_navigator
        self.driver = self.web_navigator.get_driver()

    