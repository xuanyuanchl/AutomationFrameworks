# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''
from selenium.webdriver.common.by import By

from Control.Button import button
from Control.TextField import textField
from PageBase.pageBase import pageBase


class loginPage(pageBase):
    def __init__(self):
        super().__init__('^/logon$')

    @property
    def UserName(self):
        return textField(self.webDriver, {By.ID: 'txtUserName'})

    @property
    def Password(self):
        return textField(self.webDriver, {By.ID: 'txtPassword'})

    @property
    def Enter(self):
        return button(self.webDriver, {By.ID: 'btnLogin'})
