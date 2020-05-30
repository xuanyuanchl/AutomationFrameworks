# -*- coding: utf-8 -*-
"""
Created on May 27, 2020

@author: O5LT
"""

from Control.ClickableUi import clickableUi


class radio(clickableUi):

    @property
    def IsSelected(self):
        return self.wrappedElement.is_selected()

    def Select(self):
        if not self.IsSelected:
            self.wrappedElement.click()

