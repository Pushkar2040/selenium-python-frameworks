import utilities.customlogger as cl
import logging
from base.basepage import BasePage
import time

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _search_box = "//input[@placeholder='Search Course']"
    _search_icon = "//button[@class='find-course search-course']"
    _course = "//div[@id='course-list']//h4[contains(text(),'{0}')]"
    _all_courses = "course-list"
    _enroll_button_one = "//button[@class='dynamic-button btn btn-default btn-lg btn-enroll']"
    _cc_num = "//input[@placeholder='Card Number']"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _submit_enroll = "//button[@class='zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button']"
    #_enroll_error_message = "//div[@class='card-errors has-error']//span", "xpath"


    ############################
    ### Element Interactions ###
    ############################

    def enterCourseName(self, name):
        self.sendkeys(name, locator=self._search_box, locatorType="xpath")
        self.elementclick(locator=self._search_icon,locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementclick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButtonone(self):
        self.elementclick(locator=self._enroll_button_one, locatorType="xpath")

    def enterCardNum(self, num):
        self.SwitchFrameByIndex(locator=self._cc_num,locatorType="xpath")
        self.sendkeys(num, locator=self._cc_num,locatorType="xpath")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.SwitchFrameByIndex(locator=self._cc_exp,locatorType="name")
        self.sendkeys(exp, locator=self._cc_exp,locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.SwitchFrameByIndex(locator=self._cc_cvv,locatorType="name")
        self.sendkeys(cvv, locator=self._cc_cvv,locatorType="name")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementclick(locator=self._submit_enroll, locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourseOne(self, num="", exp="", cvv=""):
        self.clickOnEnrollButtonone()
        time.sleep(2)
        self.webScroll(direction="down")
        time.sleep(2)
        self.enterCreditCardInformation(num, exp, cvv)


    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath", info="enroll button")
        return not result

    def clickwebup(self):
        self.webScroll(direction="up")