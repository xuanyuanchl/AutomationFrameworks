'''
Created on Jan 19, 2020

@author: O5LT
'''
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GetSessionAndToken():
    def __init__(self):
        # 启用无头模式，可选
        browser_options = webdriver.ChromeOptions()
        self.browser = webdriver.Chrome(options=browser_options)
        print(f"sessionid为： " + self.browser.session_id)

    # 登录系统，具体到自己系统时需要自行修改
    def login_system(self):
        # 登录用户名密码，改成目标系统用户名密码
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

    # 获取sessionid
    def get_sessionid(self):
        # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
        # window.sessionStorage和直接写sessionStorage是等效的
        # 一定要使用return，不然获取到的一直是None
        # get的Item不一定就叫sessionId，得具体看目标系统把sessionid存到哪个变量中
        cookie = self.browser.get_cookie('ASP.NET_SessionId')
        session_id = cookie['value']
        # 另外sessionid一般都直接通过返回Set-Cookies头设置到Cookie中，所以也可以从Cookie读取
        # 获取浏览器所有Set-Cookie，返回对象是字典列表
        # cookies = self.browser.get_cookies()
        # 获取单项Cookie，是不是叫sessionId取决于系统存成什么变量，单项Cookie是字典
        # cookie = self.browser.get_cookie("sessionId")
        # cookie = cookie["value"]
        # print(f"{cookies}")
        return session_id

    # 获取token
    def get_token(self):
        # 是要从localStorage中获取还是要从sessionStorage中获取，具体看目标系统存到哪个中
        # window.sessionStorage和直接写sessionStorage是等效的
        # 一定要使用return，不然获取到的一直是None
        # get的Item不一定就叫token，得具体看目标系统把token存到哪个变量中
        cookie = self.browser.get_cookie('__RequestVerificationToken')
        token_value = cookie['value']

        return token_value

    def __del__(self):
        # 退出程序时关闭浏览器
        self.browser.close()


if __name__ == "__main__":
    OBJ = GetSessionAndToken()
    OBJ.login_system()
    SESSIONID = OBJ.get_sessionid()
    TOKENVALUE = OBJ.get_token()
    print(f"sessionid为： {SESSIONID}\n"
          f"token为：     {TOKENVALUE}")
