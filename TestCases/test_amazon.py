import pytest

from Common import Browser
from PO.Am import Product, Search
from PO import Amazon

product_name = ["Amazon","Facebook"]
browse_name = {"ff":"ff","gc":"gc","ie":"ie","ed":"Edge"}
url = {"am":"https://www.amazon.com","fb":"https://www.facebook.com"}


@pytest.fixture(scope="module")
def browser_setup():
    browser = Browser.OpenBrowser().open(browse_name["ff"])
    yield browser
    # browser .quit()


def test_verify_home_page(browser_setup):
    """
    Aim of this test case is , opening amazon home page
    :return:
    """
    Amazon.open_home_page(browser_setup, url["am"], product_name[0])


def test_logged_out_user_can_search_product(browser_setup):
    """
    Aim of the test case is, search for product.
    :param setup:
    :return:
    """
    Amazon.open_home_page(browser_setup, url["am"], product_name[0])
    Amazon.search_product(browser_setup,"HP Lap top computes")


def test_logged_out_user_can_select_product(browser_setup):
    """
    Aim of the test case is, search for product, select product from product search list
    :param setup:
    :return:
    """
    Amazon.open_home_page(browser_setup, url["am"], product_name[0])
    Amazon.search_product(browser_setup, "HP Lap top computers")
    Amazon.select_product(browser_setup)


def test_logged_out_user_can_add_product_to_cart(browser_setup):
    """
    Aim of the test case is, search for product, select product from product search list
    and add to the cart
    :param setup:
    :return:
    """
    Amazon.open_home_page(browser_setup, url["am"], product_name[0])
    Amazon.search_product(browser_setup, "HP Lap top computers")
    Amazon.select_product(browser_setup)
    Amazon.add_to_cart(browser_setup)
    Amazon.verify_cart(browser_setup)


def test_logged_out_user_should_login_to_checkout(browser_setup):
    Amazon.open_home_page(browser_setup, url["am"], product_name[0])
    Amazon.search_product(browser_setup, "iphone 7s plus")
    Amazon.select_product(browser_setup)
    Amazon.add_to_cart(browser_setup)
    Amazon.verify_cart(browser_setup)
    Amazon.proceed_to_checkout(browser_setup)

