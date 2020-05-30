# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: O5LT
"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class webDriverExtensions:

    @staticmethod
    def FindElement(driver, selector, timeoutInSeconds):
        """
        find a web element with selector in a few seconds

        :param driver: web driver
        :param selector: selector contains locator and value like:
        {By.ID: id1}
        {By.XPATH: xpath1}
        :param timeoutInSeconds: timeout in a few seconds

        :return: a web element
        """
        locator, objectstring = sorted(selector.items())[0]
        if timeoutInSeconds > 0:
            waiter = WebDriverWait(driver, timeoutInSeconds)
            try:
                return waiter.until(lambda d: d.find_element(locator, objectstring),
                                    f'Cannot find web element({locator}, {objectstring}) in {timeoutInSeconds} seconds')
            except TimeoutException:
                return None

        return driver.find_element(locator, objectstring)

    @staticmethod
    def FindElements(driver, selector, timeoutInSeconds):
        """
        find a list of web elements with selector in a few seconds

        :param driver: web driver
        :param selector: selector contains locator and value like:
        {By.ID: id1}
        {By.XPATH: xpath1}
        :param timeoutInSeconds: timeout in a few seconds

        :return: a list of web elements
        """
        locator, objectstring = sorted(selector.items())[0]
        if timeoutInSeconds > 0:
            waiter = WebDriverWait(driver, timeoutInSeconds)
            try:
                return waiter.until(lambda d: d.find_elements(locator, objectstring),
                                    f'Cannot find any web element({locator}, {objectstring}) in {timeoutInSeconds} seconds')
            except TimeoutException:
                return None

        return driver.find_elements(locator, objectstring)
