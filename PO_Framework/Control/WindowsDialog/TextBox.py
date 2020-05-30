# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: O5LT
"""
from Control.WindowsDialog.ControlBase import controlBase


class textBox(controlBase):

    @property
    def Text(self):
        self.Element.set_focus()
        return self.Element.window_text()

    @Text.setter
    def Text(self, text):
        self.Element.set_focus()
        self.Element.set_edit_text(text)