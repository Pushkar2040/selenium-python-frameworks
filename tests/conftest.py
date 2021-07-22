import pytest
from selenium import webdriver
from base.webdriverfactory import webdriverfactory
from pages.home.login_page import Testloginpages

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")

    wob = webdriverfactory(browser)
    driver = wob.getwebdriverinstant()
    lp = Testloginpages(driver)
    lp.login("test@email.com", "abcabc")


    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")