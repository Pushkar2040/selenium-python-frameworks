from pages.course.registercoursepage import RegisterCoursesPage
from utilities.teststatus import teststatus
import unittest
import pytest
from ddt import ddt,data,unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesMultipleTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = teststatus(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners","21","1228","100"),("Selenium WebDriver With Python 3.x","21","1229","200"))
    @unpack
    def test_invalidEnrollment(self,Coursename, ccNum, ccExp, ccCVV):
        self.courses.enterCourseName(Coursename)
        self.courses.selectCourseToEnroll(Coursename)
        self.courses.enrollCourseOne(num=ccNum, exp=ccExp, cvv=ccCVV)
        result = self.courses.verifyEnrollFailed()
        self.ts.markfinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")
        self.courses.clickAllcourses()