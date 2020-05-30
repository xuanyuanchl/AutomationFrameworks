# -*- coding: utf-8 -*-
"""
Created on May 27, 2020

@author: O5LT
"""

from selenium.webdriver.support.select import Select
from asq import query

from Control.ControlBase import controlBase
from Control.DropdownOption import dropdownOption


class dropdown(controlBase):

    def __init__(self, driver, selector: dict = None, element=None):
        super().__init__(driver, selector, element)
        self.__selectElement = Select(self.wrappedElement)

    @property
    def SelectedLabel(self):
        return self.__selectElement.first_selected_option.text.strip()

    @property
    def SelectedValue(self):
        return self.__selectElement.first_selected_option.get_attribute('value')

    @property
    def AllSelectedOptions(self):
        return self.__selectElement.all_selected_options

    def SelectByText(self, text):
        self.__selectElement.select_by_visible_text(text)

    def DeSelectByText(self, text):
        self.__selectElement.deselect_by_visible_text(text)

    def SelectByTextLike(self, text):
        options = self.__selectElement.options
        for option in options:
            if option.text.Contains(text):
                self.__selectElement.select_by_visible_text(option.text)
                return
        raise AssertionError(f'No option found with such text {text}.')

    def SelectByValue(self, value):
        self.__selectElement.select_by_value(value)

    def DeSelectByValue(self, value):
        self.__selectElement.deselect_by_value(value)

    def SelectByIndex(self, index):
        if self.HasEmptyString:
            self.__selectElement.select_by_index(index)
        else:
            self.__selectElement.select_by_index(index - 1)

    def DeSelectByIndex(self, index):
        if self.HasEmptyString:
            self.__selectElement.deselect_by_index(index)
        else:
            self.__selectElement.deselect_by_index(index-1)

    def DeSelectAll(self):
        self.__selectElement.deselect_all()

    @property
    def AllSelectedOptions(self):
        return self.__selectElement.all_selected_options

    @property
    def AllOptions(self):
        return self.__selectElement.options

    @property
    def Labels(self):
        if self.DoesOptionExist:
            return query(self.AllOptions) \
                .select(lambda option: option.text.strip()).where(lambda label: label != '').to_list()
        else:
            return []

    @property
    def HasEmptyString(self):
        if self.DoesOptionExist:
            return query(self.AllOptions) \
                .select(lambda option: option.text.strip()).any(lambda label: label == '')
        else:
            return True

    @property
    def Options(self):
        return query(self.AllOptions).select(lambda e: dropdownOption(self.webDriver, None, e))

    @property
    def Values(self):
        if self.DoesOptionExist:
            return query(self.AllOptions) \
                .select(lambda option: option.get_attribute('value')).where(lambda value: value != '').to_list()
        else:
            return []

    @property
    def IsMultiSelectDropDown(self):
        return self.__selectElement.is_multiple

    @property
    def DoesOptionExist(self):
        return self.__selectElement.options is not None
