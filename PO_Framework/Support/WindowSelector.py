# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''


class windowSelector():
    __driver = None
    __originalWindowHandle = None

    def __init__(self, driver):
        self.__driver = driver
        self.__originalWindowHandle = driver.CurrentWindowHandle

    def SelectWindowByUrl(self, windowUrl):
        windowSuccessfullySwitched = False
        current = self.__originalWindowHandle
        for handle in self.__driver.window_handles():
            self.__driver.switch_to.window(handle)
            if(windowUrl in self.__driver.URL):
                windowSuccessfullySwitched = True
                break
        if(windowSuccessfullySwitched is not True):
            self.__driver.switch_to.window(current)
            raise Exception("Unable to select window with URL: " + windowUrl)
