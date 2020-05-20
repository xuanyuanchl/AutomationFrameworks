# -*- coding: utf-8 -*-

'''
Created on May 9, 2020

@author: O5LT
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

class controlBase():
    __driver: webdriver
    __selector = None
    __actions = None

    def __init__(self, driver, selector: dict):
        '''selector contains locator and value like:
        (by.id: id1)
        (by.xpath: xpath1)'''
        self.__driver = driver
        self.__selector = selector

    @property
    def Selector(self):
        return self.__selector

    @property
    def isVisible(self):
        return self.wrappedElement is not None and self.wrappedElement.is_displayed()

    @property
    def isPresent(self):
        return self.wrappedElement is not None

    @property
    def isEnabled(self):
        return self.wrappedElement.is_enabled()

    def getText(self):
        return self.wrappedElement.text

    @property
    def wrappedElement(self):
        try:
            locator = list(self.Selector.keys())[0]
            objectstring = list(self.Selector.values())[0]
            return self.webDriver.find_element(locator, objectstring)
        except Exception as e:
            print (str(e))
            return None

    @property
    def webDriver(self):
        return self.__driver

    @property
    def actions(self):
        if self.__actions is None:
            self.__actions = ActionChains(self.webDriver)
