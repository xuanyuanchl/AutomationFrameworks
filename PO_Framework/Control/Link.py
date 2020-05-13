# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''

from Control.ClickableUi import clickableUi


class link(clickableUi):

    @property
    def LinkText(self):
        return self.wrappedElement.text

    @property
    def Title(self):
        return self.wrappedElement.get_attribute('title')
