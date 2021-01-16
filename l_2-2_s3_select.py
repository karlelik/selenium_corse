#!/usr/bin/env python
# coding: utf-8

# In[15]:


from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome('/Games/Chromedriver.exe')
    browser.get(link)
    
    num1 = browser.find_element_by_id("num1")
    x = num1.text
    num2 = browser.find_element_by_id("num2")
    y = num2.text
    res = int(x) + int(y)

    sel1 = browser.find_element_by_id("dropdown")
    sel1.click()
    
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(res))
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
   
finally:
    time.sleep(5)
    browser.quit()


# In[ ]:




