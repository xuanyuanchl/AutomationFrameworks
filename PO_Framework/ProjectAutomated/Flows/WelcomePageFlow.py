# -*- coding: utf-8 -*-
'''
Created on May 11, 2020

@author: O5LT
'''
from ProjectAutomated.Flows.HomePageFlow import homePageFlow


class welcomePageFlow(homePageFlow):
    def __init__(self, navigator, welcomepage):
        homePageFlow.__init__(self, navigator, welcomepage)

    @property
    def GetWelcomeLabelText(self):
        return self.Page.WelcomeLabel.Text
