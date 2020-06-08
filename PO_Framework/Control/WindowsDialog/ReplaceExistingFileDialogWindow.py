# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: O5LT
"""
from Control.WindowsDialog.ControlBase import controlBase
from Control.WindowsDialog.Button import button


class replaceExistingFileDialogWindow(controlBase):

    @property
    def YesButton(self):
        e = self.Element["Yes"]
        return button(e)

    def Yes(self):
        self.YesButton.Click()
