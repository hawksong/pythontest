'''
Created on 2017年12月20日

@author: user
'''
import time  
from selenium import webdriver  
  
  
driver = webdriver.Chrome()  
driver.maximize_window()  
driver.implicitly_wait(6)  
driver.get("https://tieba.baidu.com/index.html")  
time.sleep(1)  
  
target_elem = driver.find_element_by_link_text("地区")  
driver.execute_script("return arguments[0].scrollIntoView();",target_elem)