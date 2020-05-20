# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''

from Common.AutomatedTestCase import automatedTestCase
from ProjectAutomated.Pages.LoginPage import loginPage


class case2(automatedTestCase):
    def test2(self):
        start = self.GetStart('').GoToLoginPage(
            loginPage).EnterCredentials('EOLZAA', 'Tint1n')

        login = start.Login()
        self.assertEqual('Hello', login.GetWelcomeLabelText,
                         'In result 1 the label should be "Hello".')
