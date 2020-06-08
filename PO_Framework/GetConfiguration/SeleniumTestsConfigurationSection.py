# -*- coding: utf-8 -*-
"""
Created on May 13, 2020

@author: O5LT
"""

import configparser
import os


class seleniumTestsConfigurationSection():
    """this is to get selenium tests configuration value."""

    __sectionName = 'seleniumTests'
    __driver = 'driver'
    __seleniumTestsErrorsFolder = 'seleniumTestsErrorsFolder'
    __downloadedFileDirectory = 'downloadedFileDirectory'
    __timeOut = 'timeOut'
    __useSnapShot = 'useSnapShot'
    __serverUrl = 'serverUrl'
    __defaultSnapShotSaveDirectory = 'defaultSnapShotSaveDirectory'
    __configParser = None
    __eurodatConnectionString = 'eurodatConnectionString'

    def __init__(self):
        self.__configParser = configparser.ConfigParser()
        self.__configParser.read(self.__GetConfigPath, encoding='GB18030')

    @property
    def __GetConfigPath(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        return os.path.join(os.path.dirname(
            cur_path), 'TestingConfig', 'config.ini')

    @property
    def driver(self):
        return self.__configParser.get(self.__sectionName, self.__driver)

    @property
    def downloadedFileDirectory(self):
        return self.__configParser.get(self.__sectionName, self.__downloadedFileDirectory)

    @property
    def timeOut(self):
        return self.__configParser.getfloat(self.__sectionName, self.__timeOut)

    @property
    def useSnapShot(self):
        return self.__configParser.get(self.__sectionName, self.__useSnapShot)

    @property
    def serverUrl(self):
        return self.__configParser.get(self.__sectionName, self.__serverUrl)

    @property
    def defaultSnapShotSaveDirectory(self):
        return self.__configParser.get(self.__sectionName, self.__defaultSnapShotSaveDirectory)

    @property
    def eurodatConnectionString(self):
        return self.__configParser.get(self.__sectionName, self.__eurodatConnectionString)
