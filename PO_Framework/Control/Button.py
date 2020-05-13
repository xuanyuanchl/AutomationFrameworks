# -*- coding: utf-8 -*-
'''
Created on May 9, 2020

@author: O5LT
'''

from Control.ClickableUi import clickableUi


class button(clickableUi):

    @property
    def name(self):
        return self.wrappedElement.text
