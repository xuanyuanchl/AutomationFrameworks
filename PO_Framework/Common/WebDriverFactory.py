# -*- coding: utf-8 -*-
from selenium import webdriver
from GetConfiguration.SeleniumTestsConfigurationSection import seleniumTestsConfigurationSection


class webDriverFactory(object):
    """a factory to create different kind of web driver based on browser type"""

    @classmethod
    def create(cls):
        if(cls.GetBrowser().upper() == 'IE'):
            wdriver: webdriver = webdriver.Ie()
        elif(cls.GetBrowser().upper() == 'CHROME'):
            wdriver: webdriver = webdriver.Chrome()
        elif(cls.GetBrowser().upper() == 'FIREFOX'):
            wdriver: webdriver = webdriver.Firefox()
        else:
            wdriver: webdriver = None
        return wdriver

    @staticmethod
    def GetBrowser():
        '''得到浏览器'''
        configuration = seleniumTestsConfigurationSection()
        return configuration.driver
