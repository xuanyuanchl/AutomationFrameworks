'''
Created on May 11, 2020

@author: O5LT
'''
from ProjectAutomated.Flows.HomePageFlow import homePageFlow
from ProjectAutomated.Pages.AccountsManagement.CreateEditEOLUserPage.CreateEditUserPage import createEditEOLUserPage


class createEditEOLUserPageFlow(homePageFlow):
    def __init__(self, navigator, createNewUserPage: createEditEOLUserPage):
        super().__init__(navigator, createNewUserPage)
