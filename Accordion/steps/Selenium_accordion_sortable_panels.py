
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with 4 accordion sortable sections on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/accordion/#sortable")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

@when('user selects panel 4 and moves it to the position of panel 1')    
def step_impl(context):
        section_1 = context.browser.find_element_by_id("ui-id-1")
        location1 = section_1.location
        y1=location1.get('y')
        section_1_inf = context.browser.find_element_by_id("ui-id-2")
        small_height = section_1.size.get('height')
        bigger_height = section_1_inf.size.get('height')
        section_4 = context.browser.find_element_by_id("ui-id-7")
        location4 = section_4.location
        y4=location4.get('y')
        actions = ActionChains(context.browser)
        actions.drag_and_drop_by_offset(section_4,0,-small_height*3-bigger_height-10).perform()        
        time.sleep(1)
        
        
@then('ensure panel 4 is placed on the top of all other panels')    
def step_impl(context):  
        section_4 = context.browser.find_element_by_id("ui-id-7")
        section_4_expanded = section_4.get_attribute('aria-expanded')
        location4 = section_4.location
        y4=location4.get('y')
        assert(section_4_expanded == 'true')
        assert(y4 == 8)
        
        
        

