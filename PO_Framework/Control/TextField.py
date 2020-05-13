# -*- coding: utf-8 -*-

'''
Created on May 9, 2020

@author: O5LT
'''
from Control.ControlBase import controlBase


class textField(controlBase):
    def __init__(self, driver, selector):
        super().__init__(driver, selector)

    def setText(self, text):
        self.wrappedElement.clear()
        self.wrappedElement.send_keys(text)

    def clearText(self):
        self.wrappedElement.clear()

    def appendText(self, text):
        self.wrappedElement.send_keys(text)

    def getValue(self):
        return self.wrappedElement.get_attribute('value')

    def getPlaceHolder(self):
        return self.wrappedElement.get_attribute('placeholder')

    def cursorOn(self):
        self.wrappedElement.click()
