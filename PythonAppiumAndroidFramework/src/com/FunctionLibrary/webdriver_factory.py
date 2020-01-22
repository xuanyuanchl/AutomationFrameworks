"""WebdriverFractory"""
from appium import webdriver


class WebdriverFactory():
    """WebdriverFractory class"""

    driver: webdriver

    def __init__(self):
        pass

    def create(self, command_executor, desired_caps):
        '''To create a driver'''
        self.driver = webdriver.Remote(command_executor, desired_caps)
        self.driver.implicitly_wait(20)
        return self.driver
