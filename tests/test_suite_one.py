import unittest
from tests.home.login_tests import Testlogin
from tests.course.registercourse_multiple_csv import RegisterCoursesMultiplecsv

tc1 = unittest.TestLoader().loadTestsFromTestCase(Testlogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesMultiplecsv)

smoketest = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(smoketest)