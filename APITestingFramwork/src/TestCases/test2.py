'''
Created on Dec 31, 2019

@author: O5LT
'''
import unittest
from HttpMethod.Request import httpPost

class test2(unittest.TestCase):
    """getCharFonts_post"""
    def testB(self):
        url = 'http://www.webxml.com.cn/WebServices/RandomFontsWebService.asmx/getCharFonts'
        data:dict = {'byFontsLength':'6'}

        res = httpPost(url, data)

        if(isinstance(res, str)):
            self.assertTrue(True, 'exception is:' + str(res))
            print ('exception is:' + str(res))
        else:
            self.assertTrue(True, 'actual text is:' + res.text)
            print('actual text is:' + res.text)