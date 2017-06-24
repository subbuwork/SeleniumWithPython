from selenium import webdriver
from Common import Screenshot


class FacebookLoginPage(object):
    def __init__(self,driver):
        self.driver = driver

    def verify_login_with_wrong_credentials(self, user_name, password):
        print("User Name and Password".format(user_name, password))
        self.driver.find_element_by_id("email").send_keys(user_name)
        self.driver.find_element_by_id("pass").send_keys(password)
        self.driver.find_element_by_xpath("//label[@id='loginbutton']/input").click()
        self.driver.implicitly_wait(10)
        Screenshot.ScreenShot(self.driver).take_screen_shot("Facebook","login_failed_page")

    def verify_login_with_credentials(self, user_name, password):
        self.driver.find_element_by_id("email").send_keys(user_name)
        self.driver.find_element_by_id("pass").send_keys(password)
        self.driver.find_element_by_xpath("//label[@id='loginbutton']/input").click()
        Screenshot.ScreenShot(self.driver).take_screen_shot("Facebook","login_success_page")




