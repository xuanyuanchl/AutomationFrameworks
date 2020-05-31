# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: O5LT
"""
from pywinauto import application, findwindows
from pywinauto.controls.hwndwrapper import HwndWrapper
from pywinauto.win32_element_info import HwndElementInfo

from Control.WindowsDialog.ControlFinder import controlFinder


class pywinautotest(object):
    """for the method usage please read https://pywinauto.readthedocs.io/en/latest/
    or the chinese version https://www.kancloud.cn/gnefnuy/pywinauto_doc/1193035"""

    save_as_dialog = controlFinder.GetSaveAsDialog()
    save_as_dialog.Element.print_control_identifiers(2)
    save_as_dialog.SetFocus()
    save_as_dialog.DrawOutline('red')
    save_as_dialog.Save(u'快点啊')
    #save_as_dialog.child_window(class_name='Edit').type_keys(u'd:\你好')
    #save_as_dialog.child_window(title='&Save', class_name = 'Button').click()
    # save_as_dialog["Edit"].type_keys(r'd:\1')
    # save_as_dialog["Save"].click()

    # app1 = application.Application(backend='uia').connect(class_name='IEFrame', timeout= 5)
    # ie = app1.window(class_name='IEFrame')
    # notificationBar = ie.child_window(class_name='Frame Notification Bar')
    # notificationBar.set_focus()
    # notificationBar.print_control_identifiers(7)
    # notification = notificationBar.child_window(class_name="DirectUIHWND")
    # notificationtoolbar = notificationBar.child_window(title="Notification", auto_id="IENotificationBar", control_type="ToolBar")
    # notificationtoolbar.draw_outline()
    # notificationBar.child_window(title="Open", control_type="SplitButton").click_input()

    # confirm_save_as_dialog = app1.window(title_re='Confirm Save As')
    # confirm_save_as_dialog["Yes"].click()
    # e = findwindows.find_element(process=47916)
    # p = HwndWrapper(e).top_level_parent()
    # print(HwndWrapper(e).get_properties())
