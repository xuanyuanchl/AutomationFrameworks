from selenium import webdriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome()
webdriver.get("https://www.baidu.com")
stepresult: str = None


def get_result(func):  # 此函数的作用时接受被修饰的函数的引用find_element，然后被内部函数使用
    def make_decorator():
        print('现在开始装饰')
        try:
            func()
            stepresult = 'Pass'
        except:
            stepresult = 'Error'
        finally:
            print('现在结束装饰')
            print(stepresult)
            webdriver.close()

    return make_decorator  # get_result()被调用后，运行此函数返回make_decorator()函数的引用make_decorator


@get_result  # 此行代码等同于，find_element=get_result(find_element)=make_decorator
def find_element():
    element = webdriver.find_element(By.ID, "xx")
    style_yellow = 'arguments[0].style.border="5px solid yellow"'
    webdriver.execute_script(style_yellow, element)
    print("我在find element")


if __name__ == '__main__':
    find_element()
