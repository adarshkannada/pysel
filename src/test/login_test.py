import os

import pytest
from loguru import logger

from src.main.base.base import Base
from src.main.utils.util import Util
from src.main.pages.login_page import LoginPage


class LoginTest(Base):

    def setup_method(self, method):
        # Initialize the driver before each test method
        self.initialise_driver()

    def teardown_method(self, method):
        # Quit the driver after each test method
        self.quit_driver()

    @pytest.mark.login
    def test_reject_cookie(self):

        LoginPage().reject_cookie()
