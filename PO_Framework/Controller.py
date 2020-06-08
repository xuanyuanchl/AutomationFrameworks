# -*- coding: utf-8 -*-
"""
Created on May 13, 2020

@author: O5LT
"""

import datetime
import os
import unittest
import HTMLTestRunner

from MailSender.mail_sender import SendMail


class contoller:
    """
    a controller to execute all test cases and generate html report
    """

    @property
    def CurrentTime(self) -> str:
        return datetime.datetime.strftime(
            datetime.datetime.now(), '%m%d_%H%M%S')

    @property
    def Suite(self):
        return unittest.defaultTestLoader.discover(
            os.getcwd() + '/tests', pattern='testcase*.py')


if __name__ == '__main__':
    executor = contoller()
    testResultsFolder = os.path.join(
        os.getcwd(), "./TestResults")
    if not os.path.exists(testResultsFolder):
        os.makedirs(testResultsFolder)
    html_report = testResultsFolder + "/test_report_" + executor.CurrentTime + ".html"
    with open(html_report, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            verbosity=2,
            title='EOL test',
            description='This demonstrates the report output by HTMLTestRunner.',
            tester='陈海龙')
        runner.run(executor.Suite)

    s = SendMail(html_report)
    s.send()
