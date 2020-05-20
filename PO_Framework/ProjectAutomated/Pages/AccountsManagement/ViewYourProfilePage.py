# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''
from selenium.webdriver.common.by import By

from Control.ClickableUi import clickableUi
from Control.Link import link
from Control.TextField import textField
from ProjectAutomated.HomePage import homePage


class viewYourProfilePage(homePage):
    def __init__(self):
        super(viewYourProfilePage, self).__init__('^/|/account-management#/your-profile$')

    @property
    def EditYourProfile(self):
        return link(self.webDriver, {By.ID: 'editYourProfileLink'})

    @property
    def SearchText(self):
        return textField(self.webDriver, {By.ID: 'clientSearchTextBox'})

    @property
    def Name(self):
        return clickableUi(self.webDriver, {By.ID: 'name'})

