import os
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import ActionChains
from loguru import logger
from dotenv import load_dotenv


# @pytest.mark.usefixture("driver")
class Base:
    """ the parent class contains common methods """

    def __init__(self, driver):
        # HOST = "localhost"
        load_dotenv()
        self.driver = driver

    def click_element(self, locator: any):
        (WebDriverWait(self.driver, 10).
         until(ec.visibility_of_element_located(locator=locator)).click())

    def send_values(self, locator: any, value: str):
        (WebDriverWait(self.driver, 10).
         until(ec.visibility_of_element_located(locator=locator)).send_keys(value))

    def get_element_text(self, locator: any):
        element = WebDriverWait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator=locator))
        return element

    def is_element_visible(self, locator: any):
        element = WebDriverWait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator=locator))
        return bool(element)

    def get_title(self, title: str):
        WebDriverWait(self.driver, timeout=10).until(ec.title_is(title))
        return self.driver.title


@pytest.mark.usefixtures("driver")
class Test_fire:

    def test_open_url(self, driver):
        driver.get(os.environ.get("URL"))
