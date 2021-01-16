#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome('/Games/Chromedriver.exe')
    browser.get(link)

    input1 = browser.find_element_by_css_selector('div.first_block input.form-control.first')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector('div.first_block .form-control.second')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('form-control.third')
    input3.send_keys("dog@dog.ru")
    input4 = browser.find_element_by_css_selector("div.second_block Input")
    input4.send_keys("+7-123-45-67")
    input5 = browser.find_element_by_css_selector("div.second_block Input.form-control.second")
    input5.send_keys("Solar System, Earth, Russia")
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()


# In[ ]:




