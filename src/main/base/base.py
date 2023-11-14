from selenium import webdriver


class Base:
    HOST = "localhost"
    driver = webdriver.Chrome()

    def open_url(self, url: str):
        self.driver.get(url)
        self.driver.quit()

    def test_chrome(self):
        capabilities = {
            "browserName": "chrome",
            "version": "119_VNC",
            "enableVNC": True,
            "enableVideo": False
        }
        chrome = webdriver.Remote(command_executor='http://{}:4444/wd/hub'.format(HOST))
        chrome.get('https://www.google.com')
        print('chrome', chrome.title)
        chrome.quit()


if __name__ == "__main__":
    Base().test_chrome()
