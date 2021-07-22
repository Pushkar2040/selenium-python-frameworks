import utilities.customlogger as cl
import logging
from base.selenium_driver import SeleniumDriver
from traceback import print_stack

class teststatus(SeleniumDriver):
    
    log = cl.customLogger(logging.INFO)
    
    def __init__(self,driver):
        
        super(teststatus, self).__init__(driver)
        self.resultlist = []

    def setresult(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("Pass")
                    self.log.info("### verified successful :: + " + resultmessage)
                else:
                    self.resultlist.append("Fail")
                    self.log.error("### verified failed :: + " + resultmessage)
                    self.screenshot(resultmessage)
            else:
                self.resultlist.append("Fail")
                self.log.error("### verified failed :: + " + resultmessage)
                self.screenshot(resultmessage)
        except:
            self.resultlist.append("Fail")
            self.log.error("### exception message :: + " + resultmessage)
            self.screenshot(resultmessage)
            print_stack()

    def mark(self,result, resultmessage):

        self.setresult(result, resultmessage)

    def markfinal(self,testname, result , resultmessage):

        self.setresult(result, resultmessage)

        if "Fail" in self.resultlist:
            self.log.error(testname +" ### Test Failed")
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info(testname +" ### Test Success")
            self.resultlist.clear()
            assert True == True
