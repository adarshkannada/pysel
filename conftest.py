import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def driver():
    # Initialize the WebDriver (you can customize this based on your needs)
    driver = webdriver.Chrome()
    yield driver
    # Teardown - close the WebDriver
    driver.quit()



