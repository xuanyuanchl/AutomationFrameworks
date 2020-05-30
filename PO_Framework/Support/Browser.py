"""
Created on May 9, 2020

@author: O5LT
"""
import time
from selenium.webdriver.common.action_chains import ActionChains
from Support.Alert import alert


class browser:
    """the action on browser, like back, forward, refresh"""

    __driver = None

    def __init__(self, driver):
        self.__driver = driver

    @property
    def ScriptExecutor(self):
        return self.__driver

    def WindowMaximize(self):
        self.__driver.maximize_window()

    @property
    def PageSource(self):
        return self.__driver.page_source

    @property
    def CurrentUrl(self):
        return self.__driver.current_url

    @property
    def PageTitle(self):
        return self.__driver.title

    def Back(self):
        self.__driver.back()

    def Forward(self):
        self.__driver.forward()

    def Refresh(self):
        self.__driver.refresh()

    @property
    def Actions(self):
        return ActionChains(self.__driver)

    def ClearBrowserCache(self):
        self.__driver.delete_all_cookies()
        time.sleep(5)
        self.__driver.close()
        time.sleep(5)

    def Alert(self):
        return alert(self.__driver)
