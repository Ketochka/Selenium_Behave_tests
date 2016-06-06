
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with 4 accordion scollapsive sections on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/accordion/#collapsible")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

@when('user ensures section 1 is expanded and clicks to collapse')    
def step_impl(context):
        section_1 = context.browser.find_element_by_id("ui-id-1")
        section_1_expanded = section_1.get_attribute('aria-expanded')
        assert(section_1_expanded == 'true')
        section_1.click()
        time.sleep(1)
        
@when('user ensures all four sections are collapsed and clicks on section 1 to expand')    
def step_impl(context):
        section_1 = context.browser.find_element_by_id("ui-id-1")
        section_2 = context.browser.find_element_by_id("ui-id-3")
        section_3 = context.browser.find_element_by_id("ui-id-5")
        section_4 = context.browser.find_element_by_id("ui-id-7")
        section_1_expanded = section_1.get_attribute('aria-expanded')
        section_2_expanded = section_2.get_attribute('aria-expanded')
        section_3_expanded = section_3.get_attribute('aria-expanded')
        section_4_expanded = section_4.get_attribute('aria-expanded')
        assert(section_1_expanded == 'false')
        assert(section_2_expanded == 'false')
        assert(section_3_expanded == 'false')
        assert(section_4_expanded == 'false')
        section_1.click()
        time.sleep(1)        
        
@then('ensure information of section 1 is displayed')    
def step_impl(context):  
        section_1 = context.browser.find_element_by_id("ui-id-1")
        string_full = 'Mauris mauris ante, blandit et, ultrices a, suscipit eget, quam. Integer ut neque. Vivamus nisi metus, molestie vel, gravida in, condimentum sit amet, nunc. Nam a nibh. Donec suscipit eros. Nam mi. Proin viverra leo ut odio. Curabitur malesuada. Vestibulum a velit eu ante scelerisque vulputate.'
        section_1_inf = context.browser.find_element_by_id("ui-id-2")
        section_1_expanded = section_1.get_attribute('aria-expanded')
        assert(section_1_expanded == 'true')
        assert(section_1_inf.text == string_full)
        
        

