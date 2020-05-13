# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''
from selenium.webdriver.common.by import By

from Control.Label import label
from ProjectAutomated.HomePage import homePage


class welcomePage(homePage):
    def __init__(self):
        super().__init__('^/$')

    @property
    def WelcomeLabel(self):
        return label(self.webDriver, {By.ID: 'hello'})
