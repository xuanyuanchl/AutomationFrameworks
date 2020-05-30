# -*- coding: utf-8 -*-
"""
Created on May 27, 2020

@author: O5LT
"""

from Control.ClickableUi import clickableUi


class img(clickableUi):

    @property
    def Src(self):
        return self.wrappedElement.get_attribute('src')

    @property
    def Title(self):
        return self.wrappedElement.get_attribute('title')

    @property
    def Alt(self):
        return self.wrappedElement.get_attribute('alt')
