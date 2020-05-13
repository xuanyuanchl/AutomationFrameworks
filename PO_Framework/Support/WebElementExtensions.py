# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''
from selenium.webdriver.support.wait import WebDriverWait


class webElementExtensions():
    @classmethod
    def FindElement(cls, driver, selector, timeoutInSeconds):
        if(timeoutInSeconds > 0):
            waiter = WebDriverWait(driver, timeoutInSeconds)
            locator = list(selector.keys())[0]
            objectstring = list(selector.values())[0]
            waiter.until(lambda d: d.find_element(locator, objectstring))
        return driver.find_element(locator, objectstring)

    @classmethod
    def ScrollToView(cls, element, driver):
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
