'''
Created on Jan 21, 2020

@author: O5LT
'''
import time
from sessionInfo.ReuseChrome import ReuseChrome


# 使用ReuseChrome()复用上次的session
browser2 = ReuseChrome('http://127.0.0.1:62926',
                       '5c227f8a9ba638076d558ea612f54053')
browser2.find_element_by_xpath('//*[@id="su"]').click()
# 打印current_url为百度的地址，说明复用成功
print('end')
time.sleep(2)
