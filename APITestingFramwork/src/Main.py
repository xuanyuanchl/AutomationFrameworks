'''
Created on Dec 31, 2019

@author: O5LT
'''
import unittest
import HTMLTestRunner
import os
import datetime
suite1 = unittest.defaultTestLoader.discover(os.getcwd() + '/TestCases', pattern='test*.py')
currentTime = datetime.datetime.strftime(datetime.datetime.now(), '%m%d_%H%M%S')
fp = open(os.getcwd() + "/TestResult/test_report_" + currentTime + ".html", 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='My API test',
            description='This demonstrates the report output by HTMLTestRunner.')
runner.run(suite1)
fp.close()
