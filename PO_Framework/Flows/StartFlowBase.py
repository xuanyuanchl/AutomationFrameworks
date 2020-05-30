# -*- coding: utf-8 -*-

"""
Created on May 10, 2020

@author: O5LT
"""
from Flows.FlowBase import flowBase


class startFlowBase(flowBase):
    '''
    page flow start
    '''

    def GoToPage(self, targetPage, targetPageFlow):
        """
        navigate to the target page
        :param targetPage: the page class name in ProjectAutomated.Pages
        :param targetPageFlow: the page flow class name of corresponding target page
        :return: the page flow instance, like welcomePageFlow(navigator, page)
        """
        firstPage = self.Navigator.Open(targetPage)
        return targetPageFlow(flowBase.Navigator, firstPage)
