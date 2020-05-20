# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''
from ProjectAutomated.Flows.HomePageFlow import homePageFlow

class viewYourProfilePageFlow(homePageFlow):
    def __init__(self, navigator, viewyourProfilePage):
        homePageFlow.__init__(self, navigator, viewyourProfilePage)

    @property
    def GetSearchText(self):
        self.Page.SearchText.getValue()


