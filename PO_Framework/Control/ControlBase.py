# -*- coding: utf-8 -*-

'''
Created on May 9, 2020

@author: O5LT
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


class controlBase():
    __driver: webdriver
    __selector = None
    __wrappedElement: WebElement
    __actions = None

    def __init__(self, driver, selector: dict):
        '''selector contains locator and value like:
        (by.id: id1)
        (by.xpath: xpath1)'''
        self.__driver = driver
        self.__selector = selector

    def Selector(self):
        return self.__selector

    def isVisible(self):
        return self.__wrappedElement is not None and self.__wrappedElement.is_displayed()

    def isPresent(self):
        return self.__wrappedElement is not None

    def isEnabled(self):
        return self.__wrappedElement.is_enabled()

    def getText(self):
        return self.__wrappedElement.text

    @property
    def wrappedElement(self):

        if(self.Selector() is None):
            return None

        try:
            locator = list(self.Selector().keys())[0]
            objectstring = list(self.Selector().values())[0]
            return self.webDriver.find_element(locator, objectstring)
        except Exception as e:
            return None

    @property
    def webDriver(self):
        return self.__driver

    @property
    def actions(self):
        if self.__actions is None:
            self.__actions = ActionChains(self.webDriver)
