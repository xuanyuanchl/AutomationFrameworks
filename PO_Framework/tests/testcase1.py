# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: O5LT
"""

from Common.AutomatedTestCase import automatedTestCase
from ProjectAutomated.Pages.LoginPage import loginPage


class case1(automatedTestCase):
    def test1(self):
        start = self.GetStart('').GoToLoginPage(
            loginPage).EnterCredentials('monoAdmin', 'ordAdmin1Sel')

        login = start.Login().GoToUserProfileMenu()
        self.assertFalse(login.IsOperator, 'In result 1, it should not be login as operator.')

        result = login.ViewYourProfileDetailsPage()
        expectedResult = 'Mr. CustomerUserAdmin LastName'
        self.assertEqual(expectedResult, result.Page.Name.wrappedElement.text,
                         f'In result 1, the name  "{expectedResult}" should be displayed.')

