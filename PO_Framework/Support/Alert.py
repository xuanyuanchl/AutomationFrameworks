"""
Created on May 27, 2020

@author: O5LT
"""
from selenium.common.exceptions import NoAlertPresentException


class alert:
    def __init__(self, driver):
        self.__driver = driver

    def Accept(self):
        self.__driver.switch_to_alert().accept()

    def Dismiss(self):
        self.__driver.switch_to_alert().dismiss()

    def SendKeys(self, keysToSend):
        self.__driver.switch_to_alert().send_keys(keysToSend)

    @property
    def Text(self):
        return self.__driver.switch_to_alert().text

    @property
    def IsPresent(self):
        try:
            self.__driver.switch_to_alert()
            return True
        except NoAlertPresentException:
            return False
