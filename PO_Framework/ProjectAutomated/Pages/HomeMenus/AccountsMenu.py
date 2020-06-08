# -*- coding: utf-8 -*-
"""
Created on May 11, 2020

@author: O5LT
"""
from selenium.webdriver.common.by import By
from Control.Link import link
from ProjectAutomated.HomePage import homePage


class accountsMenu(homePage):
    def __init__(self):
        super(accountsMenu, self).__init__('')

    @property
    def CreateNewUserBeta(self):
        return link(self.webDriver, {By.ID: 'create-user'})
