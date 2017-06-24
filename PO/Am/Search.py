from selenium import webdriver
from Common import Screenshot


class ProductSearch(object):

    def __init__(self,driver):
        self.driver = driver

    def search_product(self, product_name):
        """
        This method used to search for product
        :param product_name:
        :return:
        """
        print "Search key:", product_name
        self.driver.find_element_by_id("twotabsearchtextbox").send_keys(product_name)
        self.driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
        print "Page Title:", self.driver.title
        # assert self.driver.title == "Amazon.com: " + product_name, "Product search not success.."
        Screenshot.ScreenShot(self.driver).take_screen_shot("Amazon", "search_results_page")

    def select_product(self):
        """
        This method is used to select product from search results
        """
        # self.driver.find_element_by_xpath("//*[@id='nav-search']/form/div[2]/div/input").click()
        # print "Page Title::", self.driver.title
        self.driver.find_element_by_xpath("//ul[@id='s-results-list-atf']/li[3]/div/div/div/div[1]/div/div/a").click()
        Screenshot.ScreenShot(self.driver).take_screen_shot("Amazon", "product_page")