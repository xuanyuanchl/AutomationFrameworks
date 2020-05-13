# -*- coding: utf-8 -*-

'''
Created on May 11, 2020

@author: O5LT
'''
from ProjectAutomated.EOLFlow import eolFlow
from ProjectAutomated.Flows.WelcomePageFlow import welcomePageFlow
from ProjectAutomated.Pages.WelcomePage import welcomePage


class loginPageFlow(eolFlow):
    def __init__(self, navigator, loginpage):
        super().__init__(navigator, loginpage)

    def EnterCredentials(self, userName, password):
        self.Page.UserName.setText(userName)
        self.Page.Password.setText(password)
        return self

    def Login(self):
        welcomepage = self.Navigator.Navigate(
            welcomePage, self.Page.Enter.Click)
        welcomepageFlow = welcomePageFlow(self.Navigator, welcomepage)
        return welcomepageFlow
