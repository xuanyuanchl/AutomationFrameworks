# -*- coding: utf-8 -*-
'''
Created on May 9, 2020

@author: O5LT
'''

from selenium.webdriver.support.wait import WebDriverWait
from PIL import ImageGrab
from GetConfiguration.SeleniumTestsConfigurationSection import seleniumTestsConfigurationSection
from Support.Helper import helper


class navigator():
    __driver = None
    __siteUrl = None
    __helper = None
    PageLoadTimeout = None
    page = None
    FileDownloadDirectory = None

    def Open(self, targetPage):
        """open an target page"""
        target = targetPage()
        self.initPage(target)
        self.__driver.get(self.__siteUrl)
        self.Helper.Browser.WindowMaximize()
        self.__CheckPageCrashing()
        self.WaitForTargetPageLoad(target)
        self.page = target
        return target

    def Start(self, siteUrl, webDriver):
        """set site url and get web driver"""
        self.__siteUrl = siteUrl
        self.__driver = webDriver

    def initPage(self, pagebase):
        pagebase.webDriver = self.__driver

    def Navigate(self, targetPage, action=None):
        """
        execute an action like click one link to redirect to target page
        :param targetPage: the page class name in ProjectAutomated.Pages
        :param action: normally is click action
        :return: the page instance, like welcomePage()
        """
        target = targetPage()
        self.initPage(target)
        if action is not None:
            action()
        self.__CheckPageCrashing()
        self.WaitForTargetPageLoad(target)
        self.page = target
        return target

    def __CheckPageCrashing(self):
        if "Server Error in '/' Application." in self.PageSource:
            self.AssertErrorMessage("Server Error in '/' Application.")

    def AssertErrorMessage(self, msg):
        if(self.ScreenShotEnabled):
            self.SaveScreenShot('error')
        raise AssertionError(msg)

    def SaveScreenShot(self, fileName):
        """
        usually, we use web driver to save screen shot, if any exception when call save_screenshot
        it will use SaveImage to save current full screen
        :param fileName: The full path you wish to save your screenshot to. This
           should end with a `.png` extension.
        :return: True/False
        """
        if self.__driver is None:
            return None
        fileName = fileName + '.png'
        try:
            self.__driver.save_screenshot(fileName)
        except Exception as e:
            self.SaveImage(fileName)

    def CompareCurrentPageUrlToTarget(self, targetPage):
        allHandles = self.__driver.window_handles
        if(len(allHandles) > 1):
            currentWindow = self.__driver.current_window_handle
            for handle in allHandles:
                self.__driver.switch_to.window(handle)
                if(targetPage.isPageLoaded()):
                    self.__driver.switch_to.window(currentWindow)
                    return True
            return False
        return targetPage.isPageLoaded()

    def WaitForTargetPageLoad(self, targetPage):
        waiter = WebDriverWait(self.__driver, self.PageLoadTimeout)
        waiter.until(
            lambda driver: self.CompareCurrentPageUrlToTarget(targetPage),
            '{0} is not loaded correctly'.format(targetPage.__class__.__name__))

    def WaitForCondition(self, condition, timeout):
        '''condition can be lambda expression or any judgment statement
        lambda x: x.find_element_by_id("someId").is_displayed()
        or element.text == u"test"; '''
        return WebDriverWait(self.__driver, timeout, 1).until(condition)

    @property
    def Helper(self):
        if self.__helper is None:
            self.__helper = helper(self.__driver)
        return self.__helper

    @property
    def PageSource(self):
        return self.Helper.Browser.PageSource

    def ResetHelper(self):
        __helper = None

    def Dispose(self):
        if self.__driver is not None:
            self.__driver.quit()

    @property
    def _GetConfigurationSettings(self):
        return seleniumTestsConfigurationSection()

    @property
    def ScreenShotEnabled(self):
        return self._GetConfigurationSettings.useSnapShot

    def SaveImage(self, filename):
        imagegrab = ImageGrab.grab()
        imagegrab.save(filename)
