# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''
import os
from Common.DriverTestFixture import DriverTestFixture
from GetConfiguration.SeleniumTestsConfigurationSection import seleniumTestsConfigurationSection

class automatedTestCase(DriverTestFixture):

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if (error and self.ScreenShotEnabled):
                case_name = self._testMethodName
                imagesfolder = os.path.join(
                    os.getcwd(), "TestResults", "images")
                if not os.path.exists(imagesfolder):
                    os.makedirs(imagesfolder)
                file_image_path = os.path.join(
                    os.getcwd(), "TestResults", "images", case_name +
                    "_" + self.timeStramp)
                self.navigat.SaveScreenShot(file_image_path)
                print('screenshot:', case_name +
                      "_" + self.timeStramp + '.png')

        self.navigat.Dispose()
        self._DriverInstance.quit()

    @property
    def __GetConfigurationSettings(self):
        return seleniumTestsConfigurationSection()

    @property
    def ScreenShotEnabled(self):
        return self.__GetConfigurationSettings.useSnapShot