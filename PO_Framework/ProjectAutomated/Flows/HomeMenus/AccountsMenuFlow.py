# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''

from ProjectAutomated.Flows.AccountsManagement.CreateEditEOLUserPageFlow.CreateEditEOLUserPageFlow \
    import createEditEOLUserPageFlow
from ProjectAutomated.Flows.HomePageFlow import homePageFlow
from ProjectAutomated.Pages.AccountsManagement.CreateEditEOLUserPage.CreateEditUserPage import createEditEOLUserPage
from Support.JSWaiter import jsWaiter


class accountsMenuFlow(homePageFlow):

    def __init__(self, navigator, accountsmenu):
        homePageFlow.__init__(self, navigator, accountsmenu)

    def CreateNewUserBeta(self):
        createUserPage = self.Navigator.Navigate(
            createEditEOLUserPage, self.Page.CreateNewUserBeta.Click)
        jsWaiter.WaitForAngularJsFinished(self.Page.webDriver, 15)
        return createEditEOLUserPageFlow(self.Navigator, createUserPage)
