from selenium import webdriver
from Common import Screenshot


class ProductCart(object):
    def __init__(self,driver):
        self.driver = driver

    def add_product_to_cart(self):
        """
        this is method used to add product to the cart
        :return:
        """
        try:
            self.driver.find_element_by_id("a-autoid-9-announce").click()

            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("add-to-cart-button").click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("siNoCoverage-announce").click()
            Screenshot.ScreenShot(self.driver).take_screen_shot("Amazon", "cart_page")
        except Exception:
            print "Executing cat block, since element not found.."
            self.driver.implicitly_wait(7)
            self.driver.find_element_by_id("add-to-cart-button").click()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_id("siNoCoverage-announce").click()
        else:
            print "Taking screen shot.."
            self.setup.find_element_by_id("hlb-view-cart-announce").click()
            Screenshot.ScreenShot(self.driver).take_screen_shot("Amazon", "cart_page")

