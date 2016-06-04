
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with horizontal slider with fixed maximum')
def step_impl(context):
        context.browser.get("http://jqueryui.com/slider/#rangemax")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

    
@when('user selects the minimum number of bedrooms equal to one')    
def step_impl(context):
        marker = context.browser.find_element_by_xpath("//body/div[@id='slider-range-max']/span")
        marker_location = marker.location
        start = marker_location.get('x')
        actions = ActionChains(context.browser)
        actions.drag_and_drop_by_offset(marker,(-start),0)
        actions.perform()
        time.sleep(1)
        

@then('number 1 is displayed')    
def step_impl(context):    
        marker = context.browser.find_element_by_xpath("//body/div[@id='slider-range-max']/span")
        result = marker.get_attribute('style')
        assert(result=='left: 0%;')

