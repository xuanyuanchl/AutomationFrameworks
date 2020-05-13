# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''
import os

from Common.DriverTestFixture import DriverTestFixture


class automatedTestCase(DriverTestFixture):

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if (error):
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

    def __GetConfigurationSettings(self):
        return
