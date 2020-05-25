# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''

import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.DriverTestFixture import DriverTestFixture
from GetConfiguration.SeleniumTestsConfigurationSection import seleniumTestsConfigurationSection


class automatedTestCase(DriverTestFixture):

    def tearDown(self):
        # self.AcceptAlert()
        for method_name, error in self._outcome.errors:
            if error and self.ScreenShotEnabled:
                case_name = self._testMethodName
                imagesfolder = os.path.join(
                    os.getcwd(), "TestResults", "images")
                if not os.path.exists(imagesfolder):
                    os.makedirs(imagesfolder)
                file_image_path = os.path.join(
                    os.getcwd(), "TestResults", "images", case_name +
                    "_" + self.timeStamp)
                self.navigat.SaveScreenShot(file_image_path)
                print('screenshot:', case_name +
                      "_" + self.timeStamp + '.png')
                break

        self.navigat.Dispose()
        self._DriverInstance.quit()

    @property
    def __GetConfigurationSettings(self):
        return seleniumTestsConfigurationSection()

    @property
    def ScreenShotEnabled(self):
        return self.__GetConfigurationSettings.useSnapShot

    def AcceptAlert(self):
        WebDriverWait(self._DriverInstance, 1, 0.25).until(EC.alert_is_present())
        if EC.alert_is_present():
            alert_save = self._DriverInstance.switch_to_alert()
            alert_save.accept()
