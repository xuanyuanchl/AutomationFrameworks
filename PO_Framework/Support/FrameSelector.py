# -*- coding: utf-8 -*-

'''
Created on May 9, 2020

@author: O5LT
'''


class frameSelector():
    __driver = None

    def __init__(self, driver):
        self.__driver = driver

    def SelectFrame(self, frame_reference):
        self.__driver.switch_to.frame(frame_reference)
