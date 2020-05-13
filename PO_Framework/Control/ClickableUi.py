# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''
from Control.ControlBase import controlBase


class clickableUi(controlBase):
    def Click(self, isUsingJS=False):
        if(isUsingJS):
            self.ClickUsingJavascript()
        else:
            self.wrappedElement.click()

    def ClickUsingJavascript(self):
        self.webDriver.execute_script(
            'arguments[0].click();', self.wrappedElement)

    def DoubleClick(self):
        self.actions.double_click(self.wrappedElement).perform()
