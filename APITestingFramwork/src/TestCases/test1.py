'''
Created on Dec 31, 2019

@author: O5LT
'''
import unittest
from HttpMethod.Request import httpGet
from Tools.JsonParse import jsonParse
import os, sys

class test1(unittest.TestCase):
    """getCharFonts_get"""
    def testA(self):
        #headers = { 'Accept': 'application/json', 'Content-Type': 'application/json,application/x-www-form-urlencoded'}
        jp = jsonParse()
        #C:\Users\o5lt\eclipse-workspace\APITestingFramwork\src\TestCases\test1\test1_data
        methodName = sys._getframe().f_code.co_name
        className = self.__class__.__name__
        #header值中加一下token
        #第一种方法
        #headers = { 'Authorization': 'Basic {}'.format(token值)   }
        #第二种方法
        #headers = {"Authorization":"Bearer "+token值}
        file = os.path.join(os.getcwd(), 'TestCases',  className, methodName + '_data.json')
        jsonToPython = jp.loadJson(file)
        url = jp.getValue('url')
        data = jp.getDict('byFontsLength')
        res = httpGet(url, data)
        print("\r\nIn result 1, Response code is {0}".format(res.status_code))
        self.assertEqual(200, res.status_code, '{0} is not equal to {1}'.format(200, res.status_code))
        
        if(isinstance(res, str)):
            print ('In result 2, exception is:' + str(res))
            self.assertTrue(True, 'exception is:' + str(res))            
        else:
            print('In result 2, actual text is:' + res.text)
            self.assertTrue(True, 'actual text is:' + res.text)
            