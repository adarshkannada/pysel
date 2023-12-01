import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from loguru import logger
import os
from src.main.base.base import Base
from dotenv import load_dotenv

from src.main.pages.home_page import HomePage
from src.main.pages.login_page import LoginPage


@pytest.mark.usefixture("driver")
class SignUpPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        # load_dotenv()

    def create_new_account(self, driver):
        HomePage(driver).get_reject_cookie_button().click()
        Base(driver).click_element(locator=(By.ID, HomePage(driver).sign_in_link))
        LoginPage(driver).click_element(locator=(By.XPATH, LoginPage(driver).create_new_account))

