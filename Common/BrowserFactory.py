from selenium import webdriver


class BrowserFacotry(object):
    """
    This is class act as factory for all browser,
    as requested it will return respected browser object
    """
    # browser = None
    def __init__(self, browser_name):
        global browser
        if browser_name == "ie":
            browser = webdriver.Ie()
            browser.maximize_window()
        elif browser_name == "gc":
            browser = webdriver.Chrome()
            browser.maximize_window()
        elif browser_name == "ff":
            browser = webdriver.Firefox()
            browser.maximize_window()
        else:
            browser = webdriver.Edge()
            browser.maximize_window()

    def open_browser(self):
        #browser.get(url)
        return browser
