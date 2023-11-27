import pytest
from selenium.webdriver.common.by import By

from src.main.base.base import Base


@pytest.mark.usefixture("driver")
class HomePage(Base):
    def __init__(self, driver):
        super().__init__(driver)

    def get_reject_cookie_button(self):
        reject_cooke = self.driver.find_element(By.ID, "didomi-notice-disagree-button")
        return reject_cooke

    SIGN_IN_LINK = "nav-header-login-button"

    def get_home_page_title(self, title):
        return self.get_title(title=title)

    def is_sign_in_link_exists(self):
        return self.is_element_visible(self.SIGN_IN_LINK)

    def click_sign_in(self):
        self.click_element(locator=self.SIGN_IN_LINK)
