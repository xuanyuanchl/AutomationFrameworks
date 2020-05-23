# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''

import time
import unittest

from Common.WebDriverFactory import webDriverFactory
from GetConfiguration.SeleniumTestsConfigurationSection import seleniumTestsConfigurationSection
from Navigate.Navigator import navigator
from ProjectAutomated.Flows.EOLStartFlow import eolStartFlow


class DriverTestFixture(unittest.TestCase):
    """this is to create web drive based on browser type, and get server url,
    get the page load timeout, set page url, create new navigator"""
    __serverUrl = None
    __Browser = None
    _DriverInstance = None
    navigat: navigator

    def GetStart(self, pageUrl):
        """

        :param pageUrl: the relative url using regular expression of target page, like '^/logon$'
        :return: eol start flow
        """
        self._DriverInstance = webDriverFactory.create()
        startPage = self.__serverUrl + pageUrl
        self.navigat.Start(startPage, self._DriverInstance)
        return eolStartFlow(self.navigat)

    def CreateNavigator(self):
        """
        initialize a navigator
        :return: navigator
        """
        return navigator()

    def SaveScreenShot(self, fileName):
        """
        save the screen shot when error or fail occurred
        :param fileName: screen shot name
        """
        self.navigat.SaveScreenShot(fileName)

    def setUp(self):
        configuration = seleniumTestsConfigurationSection()
        self.timeStamp = time.strftime('%Y%m%d_%H%M%S')
        self.__serverUrl = configuration.serverUrl
        self.__Browser = configuration.driver
        self.navigat = self.CreateNavigator()
        self.navigat.PageLoadTimeout = configuration.timeOut
        self.navigat.FileDownloadDirectory = configuration.downloadedFileDirectory

    def tearDown(self):
        self.navigat.Dispose()
        self._DriverInstance.quit()
