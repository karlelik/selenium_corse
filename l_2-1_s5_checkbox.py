#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome('/Games/Chromedriver.exe')
    browser.get(link)
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

 
    input1 = browser.find_element_by_css_selector("div.form-group #answer")
    input1.send_keys(y)
    
    option1 = browser.find_element_by_css_selector("div.form-check.form-check-custom #robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_css_selector("div.form-check.form-radio-custom #robotsRule")
    option2.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()

