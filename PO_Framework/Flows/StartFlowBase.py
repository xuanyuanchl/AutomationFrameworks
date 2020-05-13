# -*- coding: utf-8 -*-

'''
Created on May 10, 2020

@author: O5LT
'''
from Flows.FlowBase import flowBase


class startFlowBase(flowBase):

    def GoToPage(self, targetPage, targetPageFlow):
        firstPage = self.Navigator.Open(targetPage)
        return targetPageFlow(flowBase.Navigator, firstPage)
