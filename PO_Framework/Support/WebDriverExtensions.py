# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''

from selenium.webdriver.support.wait import WebDriverWait


class webDriverExtensions():

    @classmethod
    def FindElement(cls, driver, selector, timeoutInSeconds):
        if(timeoutInSeconds > 0):
            waiter = WebDriverWait(driver, timeoutInSeconds)
            locator = list(selector.keys())[0]
            objectstring = list(selector.values())[0]
            waiter.until(lambda d: d.find_element(locator, objectstring))
        return driver.find_element(locator, objectstring)

    @classmethod
    def FindElements(cls, driver, selector, timeoutInSeconds):
        if(timeoutInSeconds > 0):
            waiter = WebDriverWait(driver, timeoutInSeconds)
            locator = list(selector.keys())[0]
            objectstring = list(selector.values())[0]
            waiter.until(lambda d: d.find_elements(locator, objectstring) if (
                len(d.find_elements(locator, objectstring)) > 0) else None)
        return driver.find_element(locator, objectstring)
