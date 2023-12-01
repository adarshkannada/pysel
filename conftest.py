import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def driver():
    # Initialize the WebDriver (you can customize this based on your needs)
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-logging")
    options.add_argument("--enable-vnc")
    options.add_argument("enableVNC")
    caps = options.to_capabilities()

    driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                              options=options)

    driver.get(os.environ.get("URL"))
    driver.maximize_window()
    yield driver
    # Teardown - close the WebDriver
    driver.quit()



