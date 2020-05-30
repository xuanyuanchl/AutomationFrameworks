# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


def get_driver(device):
    chromedriver = PATH("../exe/chromedriver.exe")
    os.environ["webdriver.chrome.driver"] = chromedriver
    chrome_capabilities = {
        "browserName": "chrome",  # 浏览器名称
        "version": "",  # 操作系统版本
        "platform": "ANY",  # 平台，这里可以是windows、linux、andriod等等
        "javascriptEnabled": True,  # 是否启用js
        "webdriver.chrome.driver": chromedriver
    }
    driver = webdriver.Remote(command_executor=device, desired_capabilities=DesiredCapabilities.CHROME)
    driver.maximize_window()  # 将浏览器最大化
    driver.get("https://www.baidu.com/")
    return driver


class ParametrizedTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', param=None):
        super(ParametrizedTestCase, self).__init__(methodName)
        global devicess
        devicess = param
    @classmethod
    def setUpClass(cls):
        pass
        cls.driver = get_driver(devicess)
        # cls.logTest = myLog().getLog("chrome")  # 每个设备实例化一个日志记录器

    def setUp(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        pass

    def tearDown(self):
        pass

    @staticmethod
    def parametrize(testcase_klass, param=None):
        print("=========")

        testloader = unittest.TestLoader()
        testnames = testloader.getTestCaseNames(testcase_klass)
        suite = unittest.TestSuite()
        for name in testnames:
            suite.addTest(testcase_klass(name, param=param))
        return suite
