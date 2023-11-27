import os
import time

import pytest
from selenium.webdriver.common.by import By

from src.main.pages.home_page import HomePage
from src.main.base.base import Base


@pytest.mark.usefixtures("driver")
class TestHomepage:

    def test_open_url(self, driver):
        driver.get(os.environ.get("URL"))
        HomePage(driver).get_reject_cookie_button().click()
        time.sleep(2)
        print(Base(driver).is_element_visible((By.ID, HomePage(driver).SIGN_IN_LINK)))

        sign_in_link_flag = Base(driver).is_element_visible((By.ID, HomePage(driver).SIGN_IN_LINK))
        assert sign_in_link_flag == True, "sign_in link is not found"
