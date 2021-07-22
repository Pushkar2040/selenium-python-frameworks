from pages.course.registercoursepage import RegisterCoursesPage
from utilities.teststatus import teststatus
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = teststatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.enterCourseName("JavaScript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourseOne(num="2151 2541 2156 1258", exp="1228", cvv="100")
        result = self.courses.verifyEnrollFailed()
        self.ts.markfinal("test_invalidEnrollment", result,
                          "Enrollment Failed Verification")