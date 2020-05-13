# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''
from selenium.webdriver.support.wait import WebDriverWait


class jsWaiter():
    SCRIPT = """var callback = arguments[arguments.length - 1];
    var el = document.querySelector('html');
    if (!window.angular) {
        callback('False')
    }
    if (angular.getTestability) {
        angular.getTestability(el).whenStable(function(){callback('True')});
    } else {
        if (!angular.element(el).injector()) {
            callback('False')
        }
        var browser = angular.element(el).injector().get('$browser');
        browser.notifyWhenNoOutstandingRequests(function(){callback('True')});
    };"""

    @classmethod
    def JSEval(cls, driver, script):
        result = driver.execute_script(script)
        if(result is None):
            return False
        else:
            return result

    @classmethod
    def __JSWait(self, driver, script, timeout):
        waiter = WebDriverWait(driver, timeout)
        waiter.until(lambda d: jsWaiter.JSEval(driver, script))

    @classmethod
    def WaitForJQueryAjaxFinished(cls, driver, timeout=10):
        cls.__JSWait(
            driver, "return document.readyState === 'complete' && jQuery.active == 0", timeout)

    @classmethod
    def WaitForMicrosoftAjaxFinished(cls, driver, timeout=10):
        cls.__JSWait(
            driver, "return !(Sys.WebForms.PageRequestManager.getInstance().get_isInAsyncPostBack());", timeout)

    @classmethod
    def WaitForAngularJsFinished(cls, driver, timeout=10):
        waiter = WebDriverWait(driver, timeout)
        waiter.until(cls.__AngularHasFinishedProcessing(driver))

    @classmethod
    def __AngularHasFinishedProcessing(self, driver):
        result = driver.execute_async_script(self.SCRIPT)
        if(result is None):
            return False
        else:
            return result
