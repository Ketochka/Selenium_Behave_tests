
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with 4 accordion sections on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/accordion/#default")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

@when('user clicks on section 2')    
def step_impl(context):
        section_2 = context.browser.find_element_by_id("ui-id-3")
        section_2.click()
        time.sleep(1)
        
@then('ensure information of section 2 is displayed and section 1 is collapsed')    
def step_impl(context):  
        section_2 = context.browser.find_element_by_id("ui-id-3")
        string_full = 'Sed non urna. Donec et ante. Phasellus eu ligula. Vestibulum sit amet purus. Vivamus hendrerit, dolor at aliquet laoreet, mauris turpis porttitor velit, faucibus interdum tellus libero ac justo. Vivamus non quam. In suscipit faucibus urna.'
        section_2_inf = context.browser.find_element_by_id("ui-id-4")
        section_2_expanded = section_2.get_attribute('aria-expanded')
        section_1 = context.browser.find_element_by_id("ui-id-1")
        section_1_expanded = section_1.get_attribute('aria-expanded')
        section_3 = context.browser.find_element_by_id("ui-id-5")
        section_3_expanded = section_3.get_attribute('aria-expanded')
        assert(section_2_expanded == 'true')
        assert(section_1_expanded == 'false')
        assert(section_3_expanded == 'false')
        assert(section_2_inf.text == string_full)
        
        

