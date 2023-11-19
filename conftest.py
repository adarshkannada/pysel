import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    # Initialize the WebDriver (you can customize this based on your needs)
    driver = webdriver.Chrome()
    yield driver
    # Teardown - close the WebDriver
    driver.quit()
