# -*- coding: utf-8 -*-
"""
Created on May 27, 2020

@author: O5LT
"""

from Control.ClickableUi import clickableUi


class checkbox(clickableUi):

    @property
    def IsChecked(self):
        return self.wrappedElement.is_selected()

    def Check(self):
        if not self.IsChecked:
            self.wrappedElement.click()

    def Uncheck(self):
        if self.IsChecked:
            self.wrappedElement.click()
    @property
    def Value(self):
        return self.wrappedElement.get_attribute('value')
