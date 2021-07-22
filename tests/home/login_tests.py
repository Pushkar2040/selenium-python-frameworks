from pages.home.login_page import Testloginpages
from utilities.teststatus import teststatus
import unittest
import pytest
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class Testlogin(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = Testloginpages(self.driver)
        self.ts = teststatus(self.driver)

    @pytest.mark.run(order=2)
    def test_validloginpage(self):
        self.lp.login("test@email.com","abcabc")
        time.sleep(2)
        result1 = self.lp.verifygettitle()
        self.ts.mark(result1, "Title verified")
        result2 = self.lp.verifyLoginSuccessful()
        self.ts.markfinal("test_vaildloginpage",result2, "verification pr")

    @pytest.mark.run(order=1)
    def test_Invalidloginpages(self):
        self.lp.logout()
        self.lp.login("test@email.com","abcabcaaa")
        result = self.lp.verifyLoginFailed()
        assert result == True







