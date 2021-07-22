import time
import logging
import utilities.customlogger as cl
from base.basepage import BasePage

class Navigationpages(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _home = "//a[contains(@class,'dynamic-link') and contains(text(),'HOME')]"
    _All_courses = "//a[contains(@class,'dynamic-link') and contains(text(),'ALL COURSES')]"
    _support = "//a[contains(@class,'dynamic-link') and contains(text(),'SUPPORT')]"
    _My_courses = "//a[contains(@class,'dynamic-link') and contains(text(),'MY COURSES')]"
    _user = "//button[@id='dropdownMenu1']"

    def clickhome(self):
        self.elementclick(locator=self._home,locatorType="xpath")

    def clickallcourses(self):
        self.elementclick(locator=self._All_courses,locatorType="xpath")

    def clicksupport(self):
        self.elementclick(locator=self._support,locatorType="xpath")

    def clickmycourses(self):
        self.elementclick(locator=self._My_courses,locatorType="xpath")

    def clickuser(self):
        userelement = self.waitForElement(locator=self._user,locatorType="xpath",pollFrequency=1)
        self.elementclick(element=userelement)
