# -*- coding: utf-8 -*-
'''
Created on May 13, 2020

@author: O5LT
'''

import datetime
import os
import unittest
import HTMLTestRunner


suite1 = unittest.defaultTestLoader.discover(
    os.getcwd() + '/tests', pattern='testcase*.py')

currentTime = datetime.datetime.strftime(
    datetime.datetime.now(), '%m%d_%H%M%S')

fp = open(os.getcwd() + "/TestResults/test_report_" +
          currentTime + ".html", 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='EOL test',
    description='This demonstrates the report output by HTMLTestRunner.')
runner.run(suite1)

fp.close()
