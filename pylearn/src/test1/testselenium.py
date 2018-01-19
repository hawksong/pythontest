'''
Created on 2017年12月20日

@author: user
'''
    # coding=utf-8  
import time  
from selenium import webdriver  

driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get('https://www.baidu.com')  
time.sleep(1)  
    # 方法一  
try:  
    assert u"百度一下" in driver.title  
    print ('Assertion test pass.')  
except Exception as e:  
    print ('Assertion test fail.', format(e))  
      
    # 方法二  
if u"百度一下，你就知道" == driver.title :  
    print ('Assertion test pass.')  
else:  
    print ('Assertion test fail.')  
      
print (driver.title)  