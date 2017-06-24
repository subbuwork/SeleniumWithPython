from Common import BrowserFactory


class OpenBrowser(object):
    def open(self,browser_name):
        browser = BrowserFactory.BrowserFacotry(browser_name).open_browser()
        return browser
