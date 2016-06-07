
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with 4 accordion collapsive sections on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/accordion/#hoverintent")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

@when('user hovers on second panel it becomes expanded and all the other become collapsed')    
def step_impl(context):
        section_2 = context.browser.find_element_by_id("ui-id-3")
        actions = ActionChains(context.browser)
        actions.move_to_element(section_2).perform()        
        time.sleep(1)
        section_2_expanded = section_2.get_attribute('aria-expanded')
        assert(section_2_expanded == 'true')
        section_1 = context.browser.find_element_by_id("ui-id-1")
        section_1_expanded = section_1.get_attribute('aria-expanded')
        assert(section_1_expanded == 'false')
        section_3 = context.browser.find_element_by_id("ui-id-5")
        section_3_expanded = section_3.get_attribute('aria-expanded')
        assert(section_3_expanded == 'false')
        section_4 = context.browser.find_element_by_id("ui-id-7")
        section_4_expanded = section_4.get_attribute('aria-expanded')
        assert(section_4_expanded == 'false')
        
@then('ensure the third panel is expanded on hover')    
def step_impl(context):  
        section_3 = context.browser.find_element_by_id("ui-id-5")
        actions = ActionChains(context.browser)
        actions.move_to_element(section_3).perform()        
        time.sleep(1)
        section_3_expanded = section_3.get_attribute('aria-expanded')
        assert(section_3_expanded == 'true')
        section_1 = context.browser.find_element_by_id("ui-id-1")
        section_1_expanded = section_1.get_attribute('aria-expanded')
        assert(section_1_expanded == 'false')
        section_2 = context.browser.find_element_by_id("ui-id-3")
        section_2_expanded = section_2.get_attribute('aria-expanded')
        assert(section_2_expanded == 'false')
        section_4 = context.browser.find_element_by_id("ui-id-7")
        section_4_expanded = section_4.get_attribute('aria-expanded')
        assert(section_4_expanded == 'false')
        
        
        

