from selenium.webdriver.common.by import By

from src.main.base.base import Base
from src.main.locators.login_page_elements import LoginPageLocators


class LoginPage(Base):

    def reject_cookie(self):
        self.driver.find_element(By.XPATH, LoginPageLocators.REJECT_COOKIE)

    def enter_username(self, username):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
