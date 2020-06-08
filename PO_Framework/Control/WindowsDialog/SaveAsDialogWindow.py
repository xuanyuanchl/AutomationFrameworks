# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: O5LT
"""
from Control.WindowsDialog.ControlBase import controlBase
from Control.WindowsDialog.ReplaceExistingFileDialogWindow import replaceExistingFileDialogWindow
from Control.WindowsDialog.Button import button
from Control.WindowsDialog.TextBox import textBox


def ReplaceExistingFile():
    from Control.WindowsDialog.ControlFinder import controlFinder
    confirm_save_as_dialog = None
    try:
        confirm_save_as_dialog = controlFinder.GetTargetWindow(title='Confirm Save As')
    except Exception:
        return confirm_save_as_dialog
    replaceExistingFileDialog = replaceExistingFileDialogWindow(confirm_save_as_dialog)
    replaceExistingFileDialog.Yes()


class saveAsDialogWindow(controlBase):

    @property
    def FileNameTextBox(self):
        e = self.Element.child_window(class_name='Edit')
        return textBox(e)

    @property
    def SaveButton(self):
        e = self.Element.child_window(title='&Save', class_name='Button')
        return button(e)

    @property
    def CancelButton(self):
        e = self.Element.child_window(title='&Cancel', class_name='Button')
        return button(e)

    @property
    def FileName(self):
        return self.FileNameTextBox.Text

    @FileName.setter
    def FileName(self, text):
        self.FileNameTextBox.Text = text

    def Save(self, fileName=None):
        if fileName:
            self.FileName = fileName
        self.SaveButton.Click()

    def SaveAs(self, fileName):
        self.FileName = fileName
        self.Save()
        ReplaceExistingFile()

    def Cancel(self):
        self.CancelButton.Click()
