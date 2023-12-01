import time

import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from loguru import logger
import os
from src.main.base.base import Base
from dotenv import load_dotenv


@pytest.mark.usefixture("driver")
class LoginPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        load_dotenv()

    create_new_account = "//a[@id='prOu_88']//div[contains(text(),'Create a new Rakuten account (free)')]"
