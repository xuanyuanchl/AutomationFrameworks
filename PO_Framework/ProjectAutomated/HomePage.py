# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''
from selenium.webdriver.common.by import By

from Control.Link import link
from PageBase.pageBase import pageBase
from asq import query


class homePage(pageBase):
    def __init__(self, pageUrl):
        super().__init__(pageUrl)

    @property
    def AccountsManagement(self) -> link:
        return link(self.webDriver, {By.ID: 'Menu_AccountsManagement'})

    @property
    def UserProfile(self) -> link:
        return link(self.webDriver, {By.ID: 'Logged_Menu_User'})

    @property
    def OperatorTools(self) -> link:
        # 1
        # return link(self.webDriver, {By.ID: 'Menu_OperatorTools'})

        # 2
        elements = self.webDriver.find_elements(By.ID, 'Menu_OperatorTools')
        element = query(elements).first_or_default(None, lambda e: e.is_displayed())
        return link(self.webDriver, None, element)

        # 3
        # elements = webDriverExtensions.FindElements(self.webDriver, {By.ID: 'Menu_OperatorTools'}, 10)
        # element = query(elements).first_or_default(None, lambda e: e.is_displayed())
        # return link(self.webDriver, None, element)

        # 4
        # element = webDriverExtensions.FindElement(self.webDriver, {By.ID: 'Menu_OperatorTools'}, 10)
        # return link(self.webDriver, None, element)
