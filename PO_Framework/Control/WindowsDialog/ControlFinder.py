# -*- coding: utf-8 -*-
"""
Created on May 10, 2020

@author: O5LT
"""

from pywinauto import application

from Control.WindowsDialog.SaveAsDialogWindow import saveAsDialogWindow


class controlFinder:
    """for the pywinauto method usage please read https://pywinauto.readthedocs.io/en/latest/
    or the chinese version https://www.kancloud.cn/gnefnuy/pywinauto_doc/1193035"""

    @staticmethod
    def GetTargetWindow(backend='win32', **kwargs):
        """
        get the parent window

        Possible input values in kwargs are:

        class_name 具有此窗口类的元素,
        class_name_re 类与此正则表达式匹配的元素,
        parent 元素是此的子元素,
        process 在此过程中运行的元素,
        title 有这个文字的元素,
        title_re 文本与此正则表达式匹配的元素,
        top_level_only 仅限顶级元素(默认值=True),
        visible_only 仅可见元素 (默认值=True),
        enabled_only 仅启用元素 (默认值=False),
        best_match 标题与此类似的元素,
        handle 要返回的元素的句柄,
        ctrl_index 要返回的子元素的索引,
        found_index 要返回的已过滤子元素的索引,
        predicate_func 用户为自定义元素验证提供了钩子,
        active_only 仅限活动元素（默认= False）,
        control_id 具有此控件ID的元素,
        control_type 具有此控件类型的元素（字符串;用于UIAutomation元素）,
        auto_id 具有此自动化ID的元素（用于UIAutomation元素）,
        framework_id 具有此框架ID的元素（用于UIAutomation元素）

        :param backend: win32 or uia or None, 搜索时使用的后端名称（默认=None表示当前活动后端）
        :param kwargs: use the above value, like "title = 'your title', class_name = 'your class name'"
        :return:  WindowSpecification
        """
        app = application.Application(backend=backend)
        app.connect(**kwargs)
        return app.window(**kwargs)

    @staticmethod
    def GetTargetElement(e, **kwargs):
        """
        Add criteria for a control

        When this window specification is resolved it will be used
        to match against a control.

        # default to non top level windows because we are usualy
        # looking for a control
        :param e: parent element
        :param kwargs: the same way in GetTargetWindow method
        :return: WindowSpecification
        """
        return e.child_window(**kwargs)

    @staticmethod
    def GetSaveAsDialog():
        e = controlFinder.GetTargetWindow(title='Save As')
        return saveAsDialogWindow(e)

    @staticmethod
    def WaitForElement(e, wait_for, timeout=5, retry_interval=0.09):
        """
        Wait for the window to be in a particular state/states.
        :param e:
        :param wait_for:
            The state to wait for the window to be in. It can be any of the following states,
            also you may combine the states by space key:
            ‘exists’ means that the window is a valid handle
            ‘visible’ means that the window is not hidden
            ‘enabled’ means that the window is not disabled
            ‘ready’ means that the window is visible and enabled
            ‘active’ means that the window is active
        :param timeout: if the window is not in the appropriate state after this number of seconds.
        Default: pywinauto.timings.Timings.window_find_timeout = 5.
        :param retry_interval: How long to sleep between each retry.
        Default: pywinauto.timings.Timings.window_find_retry = 0.09
        """
        e.wait(wait_for, timeout, retry_interval)
