
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('page with 4 accordion collapsive sections on it and Toggle icons button')
def step_impl(context):
        context.browser.get("http://jqueryui.com/accordion/#custom-icons")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

@when('user clicks on Toggle icons button and icons disappear')    
def step_impl(context):
        button = context.browser.find_element_by_id("toggle")
        button.click()
        time.sleep(1)
        
@when('user clicks on Toggle icons button again')    
def step_impl(context):
        button = context.browser.find_element_by_id("toggle")
        button.click()
        time.sleep(1) 
        
@then('ensure custom icons are visible')    
def step_impl(context):  
        icon = context.browser.find_element_by_xpath("//span[contains(@class, 'ui-accordion-header-icon')]")
        assert(icon.is_displayed)
        
        

