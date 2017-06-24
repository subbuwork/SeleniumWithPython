from selenium import webdriver
screen_shot_location = "C:\\Users\\subbu\PycharmProjects\\Selenium\\Screenshots\\"


class ScreenShot(object):

    def __init__(self, driver):
        self.driver = driver
        global screen_shot_location

    def take_screen_shot(self, test_product, screen_name):
        if test_product == "Amazon":
            self.driver.get_screenshot_as_file(screen_shot_location + test_product+"\\" + screen_name+".png")
        elif test_product == "Facebook":
            self.driver.get_screenshot_as_file(screen_shot_location + test_product+"\\" + screen_name+".png")




