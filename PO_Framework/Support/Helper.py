# -*- coding: utf-8 -*-
"""
Created on May 9, 2020

@author: O5LT
"""

from Support.Browser import browser
from Support.FrameSelector import frameSelector
from Support.WindowSelector import windowSelector


class helper:
    __browser: browser
    __driver = None
    __frameSelector = None

    def __init__(self, driver):
        self.__driver = driver
        self.__browser = browser(self.__driver)
        self.__frameSelector = frameSelector(self.__driver)

    @property
    def Browser(self):
        return self.__browser

    @property
    def FrameSelector(self):
        return self.__frameSelector

    @property
    def WindowSelector(self):
        return windowSelector(self.__driver)
