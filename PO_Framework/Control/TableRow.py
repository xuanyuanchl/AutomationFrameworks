# -*- coding: utf-8 -*-
"""
Created on May 27, 2020

@author: O5LT
"""

from selenium.webdriver.common.by import By

from Control.TableCell import tableCell


class tableRow:
    _row: None
    _tableCells: None
    _nestedTableCount: None
    _headCount: None

    def __init__ (self, row):
        self._row = row
        self._tableCells = row.find_elements(By.XPATH, './td|./th')
        self._nestedTableCount = row.find_elements(By.TAG_NAME, 'table')
        self._headCount = row.find_elements(By.TAG_NAME, 'th')

    @property
    def TableCells(self):
        cells = []
        for tablecell in self._tableCells:
            cells.append(tableCell(tablecell))
        return cells

    @property
    def IsHeaderRow(self):
        if self._nestedTableCount == 0:
            return self._headCount > 0
        else:
            return False

    @property
    def HasNestedTable(self):
        return self._nestedTableCount > 0

    @property
    def TRElement(self):
        return self._row


