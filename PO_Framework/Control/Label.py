# -*- coding: utf-8 -*-

'''
Created on May 11, 2020

@author: O5LT
'''
from Control.ControlBase import controlBase


class label(controlBase):
    @property
    def Text(self):
        return self.wrappedElement.text

    @property
    def Value(self):
        return self.wrappedElement.get_attribute('value')
