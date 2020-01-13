import unittest
import time
from appium import webdriver
import os
class Tests1(unittest.TestCase):
    def setUp(self):
        desired_caps = { "platformName" : "Android",
                        "platformVersion" : "7.1.2",
                        'deviceName': 'Redmi 4x',
                        'udid':'192.168.0.102:5555',
                        'appPackage': 'com.miui.calculator',
                        'appActivity': 'com.miui.calculator.cal.CalculatorActivity',
                        'unicodeKeyboard': True,
                        'resetunicodeKeyboard': True,
                        'noReset': True,
                        'deviceReadyTimeout': 20,
                        'newCommandTimeout': 20,
                        'androidDeviceReadyTimeout': 20,
                        'autoAcceptAlerts' : True,
                        'autoGrantPermissions':True
                        }
        
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)
        
    def testCalculator(self):
        """计算器测试"""
        
        time.sleep(1)
        self.driver.find_element_by_id('com.miui.calculator:id/btn_7_s').click()
        self.getScreenShot()
        time.sleep(1)    
        print("\r\nIn step1, press 7")  
        self.driver.find_element_by_id('com.miui.calculator:id/btn_plus_s').click()
        self.getScreenShot()
        time.sleep(1)
        print("In step2, press +") 
        self.driver.find_element_by_id('com.miui.calculator:id/btn_1_s').click()
        self.getScreenShot()
        time.sleep(1)
        print("In step3, press 1") 
        self.driver.find_element_by_id('com.miui.calculator:id/btn_c_s').click()
        self.getScreenShot()
        time.sleep(1)
        print("In step4, press clear") 
        
    def getScreenShot(self):
        img_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '//screenshots//'
        ti = time.strftime('%m%d%H%M%S', time.localtime(time.time()))
        screen_save_path = img_folder + ti + '.png'
        self.driver.get_screenshot_as_file(screen_save_path)   

    def tearDown(self):
        self.driver.quit()