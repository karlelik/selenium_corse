#!/usr/bin/env python
# coding: utf-8

# In[17]:


from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    browser = webdriver.Chrome('/Games/Chromedriver.exe')
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    
    num = browser.find_element_by_id("input_value")
    x = num.text
    
    y = calc(x)
    
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    input1 = browser.find_element_by_css_selector("div.form-group #answer")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_css_selector("#robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("#robotsRule")
    option2.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
   
finally:
    time.sleep(5)
    browser.quit()

