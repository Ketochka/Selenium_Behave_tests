
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with horizontal slider with two markers on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/slider/#range")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

    
@when('user moves left slider and selects value $14')    
def step_impl(context):
        slider = context.browser.find_element_by_xpath("//body/div[@id='slider-range']")
        left_marker = context.browser.find_element_by_xpath("//body/div[@id='slider-range']/span[1]")
        width = slider.size['width']
        left_marker_location = left_marker.location
        l = left_marker_location.get('x')
        actions = ActionChains(context.browser)
        actions.drag_and_drop_by_offset(left_marker,(-l+width*15/500),0)
        actions.perform()
        time.sleep(1)
        
@when('user moves right slider and selects value $85')    
def step_impl(context):
        slider = context.browser.find_element_by_xpath("//body/div[@id='slider-range']")
        right_marker = context.browser.find_element_by_xpath("//body/div[@id='slider-range']/span[2]")
        width = slider.size['width']
        right_marker_location = right_marker.location
        r = right_marker_location.get('x')
        actions = ActionChains(context.browser)
        actions.drag_and_drop_by_offset(right_marker,(-r+width*86/500),0)
        actions.perform() 
        time.sleep(1)

@then('ensure marker positions on slider are correct')    
def step_impl(context):    
        left_marker = context.browser.find_element_by_xpath("//body/div[@id='slider-range']/span[1]")
        right_marker = context.browser.find_element_by_xpath("//body/div[@id='slider-range']/span[2]")
        ll = left_marker.get_attribute('style')
        rr = right_marker.get_attribute('style')
        assert(ll=='left: 2.8%;')
        assert(rr=='left: 17%;')

