#!/usr/bin/env python
# coding: utf-8

# In[3]:


from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome('\Games\chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element_by_css_selector("input.form-control[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("input.form-control[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("input.form-control[name='email']")
    input3.send_keys("Smolensk")
    
    current_dir = os.path.dirname(os.path.abspath(" __file__ "))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_css_selector('#file')
    element.send_keys(file_path)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()


# In[ ]:




