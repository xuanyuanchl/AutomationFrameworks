# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''

from ProjectAutomated.Flows.AccountsManagement.ViewYourProfilePageFlow import viewYourProfilePageFlow
from ProjectAutomated.Flows.HomePageFlow import homePageFlow
from ProjectAutomated.Pages.AccountsManagement.ViewYourProfilePage import viewYourProfilePage
from Support.JSWaiter import jsWaiter


class userProfileMenuFlow(homePageFlow):
    def __init__(self, navigator, userprofilemenu):
        homePageFlow.__init__(self, navigator, userprofilemenu)

    def ViewYourProfileDetailsPage(self):
        yourProfileDetailsPage = self.Navigator.Navigate(viewYourProfilePage, self.Page.YourProfile.Click)
        jsWaiter.WaitForAngularJsFinished(self.Page.webDriver, 60)
        jsWaiter.WaitForJQueryAjaxFinished(self.Page.webDriver, 60)
        return viewYourProfilePageFlow(self.Navigator, yourProfileDetailsPage)

    @property
    def LogoutLinkText(self):
        return self.Page.Logout.Text

    @property
    def DisclaimerLinkText(self):
        return self.Page.Logout.Text

