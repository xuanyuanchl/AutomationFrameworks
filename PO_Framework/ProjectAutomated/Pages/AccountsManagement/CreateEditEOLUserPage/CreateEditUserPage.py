# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''
from ProjectAutomated.HomePage import homePage


class createEditEOLUserPage(homePage):
    def __init__(self):
        super().__init__('^/|/account-management#/users/create')
