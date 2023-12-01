import os
import time

import pytest
from loguru import logger
from selenium.webdriver.common.by import By

from src.main.pages.home_page import HomePage
from src.main.base.base import Base
from src.main.pages.sign_up_page import SignUpPage


@pytest.mark.usefixtures("driver")
class TestSignUpPage:

    def test_sign_up_window(self, driver):
        SignUpPage(driver).create_new_account(driver)
        time.sleep(4)
        logger.info("test passed")
        