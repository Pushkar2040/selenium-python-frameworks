from pages.course.registercoursepage import RegisterCoursesPage
from utilities.teststatus import teststatus
import unittest
import pytest
from ddt import ddt,data,unpack
from utilities.read_data import getcsvdata
from pages.home.navigation_page import Navigationpages
import time

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesMultiplecsv(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = teststatus(self.driver)
        self.nav = Navigationpages(self.driver)

    def setUp(self):
        self.nav.clickallcourses()

    @pytest.mark.run(order=1)
    @data(*getcsvdata("testdata.csv"))
    @unpack
    def test_invalidEnrollmentone(self,Coursename, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName(Coursename)
        time.sleep(1)
        self.courses.selectCourseToEnroll(Coursename)
        time.sleep(1)
        self.courses.enrollCourseOne(num=ccNum, exp=ccExp, cvv=ccCVV)
        time.sleep(1)
        result = self.courses.verifyEnrollFailed()
        self.ts.markfinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        time.sleep(1)
        self.courses.clickwebup()

