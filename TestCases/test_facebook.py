import pytest

from Common import HomePage
from PO.Fb import LoginPage


@pytest.fixture(scope="module")
def setup():
    driver = HomePage.OpenPage().open("Facebook", "ff", "https://www.facebook.com")
    yield driver
    driver.quit()


def test_verify_login_failed(setup):
    """
    Aim of the test case is, to verify login functionality wrong credentials
    :param setup:
    :return:
    """
    LoginPage.FacebookLoginPage(setup).verify_login_with_wrong_credentials("test", "test123")


@pytest.mark.skip
def test_verify_lgon_success(setup):
    """
    Aim of the test case is, to verify login functionality right credentials
    :param setup:
    :return:
    """
    LoginPage.FacebookLoginPage(setup).verify_login_with_credentials("subbu.varsith1@gmail.com","Jason@2017")