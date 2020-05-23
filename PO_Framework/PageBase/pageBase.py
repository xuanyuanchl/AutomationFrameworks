# -*- coding: utf-8 -*-
'''
Created on Apr 29, 2020

@author: O5LT
'''
import re
from urllib.parse import urlparse


class pageBase():
    _pageUrl = None
    webDriver = None

    def __init__(self, pageUrl):
        self._pageUrl = self.__FormatUrl(pageUrl)

    @staticmethod
    def __FormatUrl(pageUrl):
        url = pageUrl
        if(url.startswith('~/')):
            url = url[2:]
        return url

    def isReady(self):
        isPageReady = False
        try:
            pageState = self.webDriver.execute_script(
                'return document.readyState')
            isPageReady = pageState is not None and pageState == 'complete'
        except Exception as e:
            print(str(e))
            isPageReady = False
        return isPageReady

    def isPageLoaded(self):
        currentUrl = self.webDriver.current_url
        if currentUrl is None or currentUrl == '':
            return False
        location = urlparse(currentUrl)
        path = location.path
        result = re.match(self._pageUrl, path)
        return result is not None and self.isReady()

    @property
    def CurrentPageTitle(self):
        return self.webDriver.title
