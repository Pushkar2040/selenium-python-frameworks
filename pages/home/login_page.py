import time
import logging
import utilities.customlogger as cl
from base.basepage import BasePage
from pages.home.navigation_page import Navigationpages

class Testloginpages(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = Navigationpages(driver)

    # Locators
    _login_link = "//a[@href='/login']"
    _email_path = "email"
    _password_path = "password"
    _login_button = "//input[@value='Login']"


    def clickloginlink(self):
        self.elementclick(self._login_link, "xpath")

    def sendemailpath(self, username):
        self.sendkeys(username,self._email_path)

    def sendpasswordpath(self,password):
        self.sendkeys(password,self._password_path)

    def clickloginbutton(self):
        self.elementclick(self._login_button, "xpath")

    def login(self, username="", password=""):
        self.clickloginlink()
        time.sleep(3)
        self.clearfield()
        self.sendemailpath(username)
        self.sendpasswordpath(password)
        time.sleep(3)
        self.clickloginbutton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//label[@class='dynamic-text']", "xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='form-group has-error']//span", "xpath")
        return result
    
    def clearfield(self):
        emailpath = self.getElement(locator=self._email_path,)
        emailpath.clear()
        passwordpath = self.getElement(locator=self._password_path)
        passwordpath.clear()

    def verifygettitle(self):
        return self.verifyPageTitle("All Courses")

    def logout(self):
        self.nav.clickuser()
        logoutlinkelement = self.waitForElement(locator="//a[@href='/logout']",locatorType="xpath",pollFrequency=1)
        self.elementclick(element=logoutlinkelement)



