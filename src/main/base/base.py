import os
import time

from selenium import webdriver
from loguru import logger
from dotenv import load_dotenv


class Base:

    def __init__(self):
        # HOST = "localhost"
        load_dotenv()
        self.driver = None

    def initialise_driver(self):
        # global driver
        if os.environ.get("BROWSER") == 'chrome':
            logger.info(os.environ.get("BROWSER"))
            self.driver = webdriver.Chrome()
        elif os.environ.get("BROWSER") == 'firefox':
            os.environ.get("BROWSER")
            self.driver = webdriver.Firefox()
        return self.driver

    def quit_driver(self):
        if self.driver:
            self.driver.quit()


# if __name__ == "__main__":
#     Base().initialise_driver()
