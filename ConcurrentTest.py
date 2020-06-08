# coding=utf-8
import os
import sys
import threading
import time
import unittest

import HTMLTestRunner

sys.path.append('C:/Users/Dell/Desktop/CARE/program')  # 使用编辑器，要指定当前目录，不然无法执行第20行代码


def creatsuite():
    casedir = []
    list = os.listdir(os.path.dirname(os.getcwd()))  # 获取当前路径的上一级目录的所有文件夹,这里可以改成绝对路径(要搜索的文件路径)
    for xx in list:
        if "baidu" in xx:
            casedir.append(xx)
    suite = []
    for n in casedir:
        testunit = unittest.TestSuite()
        unittest.defaultTestLoader._top_level_dir = None
        # （unittest.defaultTestLoader(): defaultTestLoader()类，通过该类下面的discover()方法可自动更具测试目录start_dir匹配查找测试用例文件（test*.py），
        discover = unittest.defaultTestLoader.discover(str(n), pattern='tet_*.py', top_level_dir=None)

        for test_suite in discover:
            for test_case in test_suite:
                testunit.addTests(test_case)
        suite.append(testunit)
    return suite, casedir


def runcase(suite, casedir):
    lastPath = os.path.dirname(os.getcwd())  # 获取当前路径的上一级
    resultDir = lastPath + "\\run\\report\\"  # 报告存放路径
    now = time.strftime("%Y-%m-%d %H.%M.%S", time.localtime())
    filename = resultDir + now + " result.html"
    fp = open(filename, 'wb')
    proclist = []
    s = 0

    for i in suite:
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=str(casedir[s]) + u'测试报告', description=u'用例执行情况：')
        proc = threading.Thread(target=runner.run, args=(i,))
        proclist.append(proc)
        s = s + 1
    for proc in proclist:
        proc.start()
    for proc in proclist:
        proc.join()
    fp.close()


if __name__ == "__main__":
    runtmp = creatsuite()
    runcase(runtmp[0], runtmp[1])
