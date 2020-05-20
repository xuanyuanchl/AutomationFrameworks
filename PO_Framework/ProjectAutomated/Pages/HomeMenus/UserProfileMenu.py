# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''
from selenium.webdriver.common.by import By
from Control.Link import link
from ProjectAutomated.HomePage import homePage


class userProfileMenu(homePage):
    def __init__(self):
        super(userProfileMenu, self).__init__('')

    @property
    def EditYourDetails(self):
        return link(self.webDriver, {By.ID: 'edit-your-profile'})

    @property
    def YourProfile(self):
        return link(self.webDriver, {By.ID: 'your-profile'})

    @property
    def Logout(self):
        return link(self.webDriver, {By.ID: 'Menu_Logout'})

    @property
    def Disclaimer(self):
        return link(self.webDriver, {By.ID: 'view-disclaimer'})
