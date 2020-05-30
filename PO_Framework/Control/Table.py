# -*- coding: utf-8 -*-
"""
Created on May 27, 2020

@author: O5LT
"""
from asq import query
from selenium.webdriver.remote import webelement

from Control.TableRow import tableRow


class table:
    tableRows: None
    wrappedElement: None

    def __init__(self, driver = None, selector: dict = None , element:webelement = None):
        """

        :param driver: web driver
        :param selector: pass the By and value in selector
        :param element: a table which is a webelement
        """
        if element is not None:
            self.wrappedElement = element
        if driver is not None and selector is not None :
            locator, objectstring = sorted(selector.items())[0]
            self.wrappedElement = driver.find_element(locator, objectstring)
        if driver == selector == element == None:
            raise AssertionError('Please specify a way to find the table, '
                                 'if using driver.find_element, please pass necessary driver and selector '
                                 'else pass the element directly.')
        self.tableRows = self.wrappedElement.find_elements('./tbody/tr|./thead/tr')

    @property
    def TableRows(self):
        rows = []
        for tablerow in self.tableRows:
            rows.append(tableRow(tablerow))
        return rows

