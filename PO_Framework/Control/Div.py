# -*- coding: utf-8 -*-
"""
Created on May 27, 2020

@author: O5LT
"""
from selenium.webdriver.remote import webelement

from Control.ControlBase import controlBase


class div(controlBase):
    def __init__(self, driver, selector: dict = None, element: webelement = None):
        super().__init__(driver, selector, element)
