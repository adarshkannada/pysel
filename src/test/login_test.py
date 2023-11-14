import os

import pytest
from loguru import logger

from src.main.base.base import Base
from src.main.utils.util import Util


class LoginTest(Base):

    @pytest.mark.login
    def test_login_page(self):
        url = os.environ.get("url")
        logger.info(url)
        Base.open_url(self, url=os.environ.get("url"))

        title = Base.driver.title
        logger.info("the page title is: " + title)
