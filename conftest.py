import os

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from loguru import logger


HOST = os.environ.get("HOST")


@pytest.fixture(scope="class")
def driver():
    # Initialize the WebDriver (you can customize this based on your needs)
    logger.info("preparing chrome options")
    options = webdriver.ChromeOptions()
    options.add_argument("--enable-logging")
    options.add_argument("--enable-vnc")
    options.add_argument("enableVideo")
    caps = options.to_capabilities()
    logger.info("browser capabilities are configured")
    logger.info("initialising chrome driver")
    driver = webdriver.Remote(command_executor="http://{}:4444/wd/hub".format(HOST),
                              options=options)
    logger.info("chrome driver initialised")
    driver.get(os.environ.get("URL"))
    logger.info("URL is opened")
    driver.maximize_window()
    logger.info("browser window is maximised")
    yield driver
    # Teardown - close the WebDriver
    driver.quit()
    logger.info("driver is closed")



