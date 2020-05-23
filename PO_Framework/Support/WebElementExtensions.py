# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class webElementExtensions():

    @staticmethod
    def FindElement(driver, selector, timeoutInSeconds):
        locator, objectstring = sorted(selector.items())[0]
        if timeoutInSeconds > 0:
            waiter = WebDriverWait(driver, timeoutInSeconds)
            try:
                waiter.until(lambda d: d.find_element(locator, objectstring))
            except NoSuchElementException as e:
                print('no such element.')
            except TimeoutException as e:
                print('find element timeout.')
        return driver.find_element(locator, objectstring)

    @staticmethod
    def ScrollToView(element, driver):
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
