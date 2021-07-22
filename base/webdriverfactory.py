import os
import traceback
from selenium import webdriver

class webdriverfactory():

    def __init__(self, browser):
        self.browser = browser

    def getwebdriverinstant(self):

        baseurl ="https://courses.letskodeit.com/"
        if self.browser == "iexplorer":
            driver = webdriver.Ie()

        elif self.browser == "firefox":
            driver = webdriver.Firefox()

        elif self.browser == "chrome":
            chromedriver = "C:/Users/srm12/workspace_python/drivers/chromedriver"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(1440,900)

        else:
            driver = webdriver.Firefox()

        driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get(baseurl)
        return driver


