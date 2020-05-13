# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''
from Flows.FlowBase import flowBase


class eolFlow(flowBase):
    __eolFlowPage = None

    def __init__(self, navigator, eolFlowPage):
        super().__init__(navigator)
        self.__eolFlowPage = eolFlowPage

    @property
    def Page(self):
        return self.__eolFlowPage
