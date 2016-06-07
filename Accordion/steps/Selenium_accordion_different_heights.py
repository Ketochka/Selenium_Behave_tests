
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

@given('page with 4 accordion collapsive sections of different height')
def step_impl(context):
        context.browser.get("http://jqueryui.com/accordion/#no-auto-height")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

@when('user checks the height of first expanded panel and clicks on the second panel')    
def step_impl(context):
        first_panel = context.browser.find_element_by_id("ui-id-2")
        y1 = first_panel.size.get('height')
        second = context.browser.find_element_by_id("ui-id-3")
        second.click()
        second_panel = context.browser.find_element_by_id("ui-id-4")
        y2 = second_panel.size.get('height')
        assert(y1 != y2)
        
        
@then('ensure the height of the third and second panels are not the same')    
def step_impl(context):  
        second_panel = context.browser.find_element_by_id("ui-id-4")
        y2 = second_panel.size.get('height')
        third = context.browser.find_element_by_id("ui-id-5")
        third.click()
        third_panel = context.browser.find_element_by_id("ui-id-6")
        y3 = third_panel.size.get('height')
        assert(y2 != y3)
        
        

