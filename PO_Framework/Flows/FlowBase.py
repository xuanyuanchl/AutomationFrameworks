# -*- coding: utf-8 -*-
'''
Created on May 9, 2020

@author: O5LT
'''

from PageBase.pageBase import pageBase


class flowBase:
    '''flow base class'''
    flowPage: pageBase

    def __init__(self, navigate):
        self._navi = navigate

    @property
    def Navigator(self):
        self.flowPage = self._navi.page
        return self._navi

    @Navigator.setter
    def Navigator(self, navi):
        self.__navigator = navi
