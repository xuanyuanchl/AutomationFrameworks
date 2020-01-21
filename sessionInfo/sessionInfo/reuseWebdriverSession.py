'''
Created on Jan 19, 2020

@author: O5LT
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from sessionInfo.ReuseChrome import ReuseChrome


class GetWebdriverSession():
    def __init__(self):
        # 启用无头模式，可选
        self.browser = webdriver.Chrome()

    # 登录系统，具体到自己系统时需要自行修改
    def login_system(self):
        # 登录用户名密码，改成目标系统用户名密码
        executor_url = self.browser.command_executor._url
        session_id = self.browser.session_id
        username = "testchl"
        password = "eurofins1"
        # 登录页面url，改成目标系统登录页面
        url = "https://qa-ci-uk1-testing.eol-test.eurofins.local/logon?ReturnUrl=%2f"
        self.browser.get(url)
        self.browser.maximize_window()

        # 显性等待，直到用户名控件加载出来才进行下一步
        WebDriverWait(self.browser, 20, 0.5).until(
            EC.presence_of_element_located((By.ID, "txtUserName")))
        # 填写用户名
        self.browser.find_element_by_id("txtUserName").send_keys(username)
        # 填写密码
        self.browser.find_element_by_id("txtPassword").send_keys(password)
        # 点击登录
        self.browser.find_element_by_id("btnLogin").click()
        # 强制等待5秒，待session和token都成功返回并存到浏览器中
        # restful隐性等待不太好用？self.browser.implicitly_wait(5)
        time.sleep(5)
        # 假如driver对象不存在，但浏览器未关闭
        del self.browser

        # 使用ReuseChrome()复用上次的session
        browser2 = ReuseChrome(executor_url, session_id)

        # 打印current_url为百度的地址，说明复用成功
        print(browser2.current_url)
        browser2.get("https://www.baidu.com")
        time.sleep(5)
        browser2.quit()


if __name__ == "__main__":
    A = GetWebdriverSession()
    A.login_system()
