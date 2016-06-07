
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

@given('page with 4 accordion collapsive sections on it and a dragging point')
def step_impl(context):
        context.browser.get("http://jqueryui.com/accordion/#fillspace")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

@when('user checks current panels width and decreases it with a dragging point')    
def step_impl(context):
        resizable_element = context.browser.find_element_by_xpath("//div[@id='accordion-resizer']")
        x = resizable_element.size.get('width')
        time.sleep(1)
        dragging_point = context.browser.find_element_by_xpath("//div[contains(@class,'ui-icon-gripsmall-diagonal-se')]")
        actions = ActionChains(context.browser)
        actions.drag_and_drop_by_offset(dragging_point,-100,0).perform()
        time.sleep(1)
        new_x=resizable_element.size.get('width')
        assert((x-new_x)==100)
        
@when('user makes the panel set to be much wider and a bit higher')    
def step_impl(context):
        resizable_element = context.browser.find_element_by_xpath("//div[@id='accordion-resizer']")
        x = resizable_element.size.get('width')
        y = resizable_element.size.get('height')
        dragging_point = context.browser.find_element_by_xpath("//div[contains(@class,'ui-icon-gripsmall-diagonal-se')]")
        actions = ActionChains(context.browser)
        actions.drag_and_drop_by_offset(dragging_point,300,100).perform()
        time.sleep(1)
        new_x=resizable_element.size.get('width')
        new_y = resizable_element.size.get('height')
        assert((new_y-y)==100) 
        
@then('ensure new width and height are set correctly')    
def step_impl(context):  
        resizable_element = context.browser.find_element_by_id("accordion-resizer")
        result = resizable_element.get_attribute('style')
        print(result)
        assert(result == 'width: 550px; height: 320px;')
        
        

