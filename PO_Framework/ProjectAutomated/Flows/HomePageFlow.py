# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: O5LT
"""
from ProjectAutomated.EOLFlow import eolFlow
from ProjectAutomated.Pages.HomeMenus.UserProfileMenu import userProfileMenu


class homePageFlow(eolFlow):
    def __init__(self, navigator, homepage):
        super(homePageFlow, self).__init__(navigator, homepage)

    def GoToUserProfileMenu(self):
        from ProjectAutomated.Flows.HomeMenus.UserProfileMenuFlow import userProfileMenuFlow
        userprofileMenu = self.Navigator.Navigate(userProfileMenu, self.Page.UserProfile.Click)
        return userProfileMenuFlow(self.Navigator, userprofileMenu)

    @property
    def IsOperator(self) -> bool:
        return self.Page.OperatorTools.isPresent
