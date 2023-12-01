import pytest
from selenium.webdriver.common.by import By

from src.main.base.base import Base


@pytest.mark.usefixture("driver")
class HomePage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    sign_in_link = "nav-header-login-button"
    create_new_account_new = "prOu_88"

    def get_reject_cookie_button(self):
        reject_cooke = self.driver.find_element(By.ID, "didomi-notice-disagree-button")
        return reject_cooke

    def get_home_page_title(self, title):
        return self.get_title(title=title)

    def click_sign_in(self):
        self.click_element(locator=self.sign_in_link)

