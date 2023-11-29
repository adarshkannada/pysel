import os
import time

import pytest
from selenium.webdriver.common.by import By

from src.main.pages.home_page import HomePage
from src.main.base.base import Base


@pytest.mark.usefixtures("driver")
class TestHomepage:

    def test_open_url(self, driver):
        # driver.get(os.environ.get("URL"))
        HomePage(driver).get_reject_cookie_button().click()
        time.sleep(2)
        print(Base(driver).is_element_visible((By.ID, HomePage(driver).sign_in_link)))

        sign_in_link_flag = Base(driver).is_element_visible((By.ID, HomePage(driver).sign_in_link))
        assert sign_in_link_flag == True, "sign_in link is not found"

    def test_sign_up(self, driver):
        driver.get(os.environ.get("URL"))
        HomePage(driver).get_reject_cookie_button().click()
        time.sleep(1)

        Base(driver).click_element(locator=(By.ID, HomePage(driver).sign_in_link))
        time.sleep(1)
