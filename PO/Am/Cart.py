from selenium import webdriver
from Common import Screenshot


class ProductCart(object):
    def __init__(self,setup):
        self.setup = setup

    def verify_cart(self):
        self.setup.find_element_by_id("hlb-view-cart-announce").click()

    def proceed_to_check_out(self):
        try:
            self.setup.find_element_by_id("hlb-ptc-btn-native").click()
        except:
            self.setup.find_element_by_xpath("//*[@id='sc-buy-box-ptc-button']/span/input").click()




