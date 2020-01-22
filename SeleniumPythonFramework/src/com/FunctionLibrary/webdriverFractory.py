from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class webdriverFactory(object):
    """create a driver"""

    script = """var callback = arguments[arguments.length - 1];
    var el = document.querySelector('html');
    if (!window.angular) {
        callback('False')
    }
    if (angular.getTestability) {
        angular.getTestability(el).whenStable(function(){callback('True')});
    } else {
        if (!angular.element(el).injector()) {
            callback('False')
        }
        var browser = angular.element(el).injector().get('$browser');
        browser.notifyWhenNoOutstandingRequests(function(){callback('True')});
    };"""

    def __init__(self):
        pass

    def create(self):
        wdriver: webdriver = webdriver.Chrome()
        wdriver.implicitly_wait(60)
        wdriver.maximize_window()
        return wdriver

    @staticmethod
    def is_Angular_Ready(driver):
        wdw = WebDriverWait(driver, 30)
        wdw.until(lambda driver: driver.execute_async_script(
            webdriverFactory.script))

    @staticmethod
    def waitforready(driver):
        wdw = WebDriverWait(driver, 30)
        # wait page load completely
        wdw.until(lambda x: driver.execute_script(
            'return document.readyState == "complete"'))
        # wait jQuery ready
        wdw.until(lambda x: driver.execute_script('return jQuery.active == 0'))
        # wait agularJs processed
        webdriverFactory.is_Angular_Ready(driver)
