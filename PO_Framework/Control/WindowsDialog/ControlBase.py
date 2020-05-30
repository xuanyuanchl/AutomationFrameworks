# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: O5LT
"""


class controlBase:

    def __init__(self, e):
        self.Element = e

    def Click(self):
        self.Element.click()

    def DoubleClick(self):
        self.Element.double_click()

    def SetFocus(self):
        self.Element.set_focus()

    def DrawOutline(self, color='green'):
        """
        Draw an outline around the window.

        * **colour** can be either an integer or one of 'red', 'green', 'blue'
          (default 'green')
        """
        self.Element.draw_outline(color)

    @property
    def GetFocus(self):
        return self.Element.get_focus()

    @property
    def GetWindowText(self):
        return self.Element.window_text()

    @property
    def IsDialog(self):
        return self.Element.is_dialog()
