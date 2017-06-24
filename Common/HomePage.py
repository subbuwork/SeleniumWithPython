from selenium import webdriver
from Common import Screenshot


class Homepage(object):
    def __init__(self, setup):
        self.setup = setup

    def open_home_page(self,url,product_name):
        self.setup.get(url)
        Screenshot.ScreenShot(self.setup).take_screen_shot(product_name, "homepage")



