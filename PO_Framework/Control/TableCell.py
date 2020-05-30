# -*- coding: utf-8 -*-
"""
Created on May 27, 2020

@author: O5LT
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement

from Control.Table import table


class tableCell:
    __cell: None
    isHeader: bool

    def __init__(self, cell: webelement):
        self.__cell = cell
        self.isHeader = cell.tag_name.lower() == 'th'

    @property
    def CellElement(self):
        return self.__cell

    @property
    def Text(self):
        return self.__cell.text

    @property
    def IsHeader(self):
        return self.isHeader

    @property
    def NestedTable(self):
        nestTable = self.CellElement.find_elements(By.XPATH, './table')
        if nestTable is not None:
            return table(None, None, nestTable[0])
        else:
            return None
