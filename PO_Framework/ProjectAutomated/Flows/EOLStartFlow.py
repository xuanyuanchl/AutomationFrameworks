# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''
from Flows.StartFlowBase import startFlowBase
from ProjectAutomated.Flows.LoginPageFlow import loginPageFlow
from ProjectAutomated.Pages.LoginPage import loginPage


class eolStartFlow(startFlowBase):
    def GoToLoginPage(self, targetPage: loginPage):
        """go to the login page"""
        login = self.Navigator.Open(targetPage)
        return loginPageFlow(self.Navigator, login)
