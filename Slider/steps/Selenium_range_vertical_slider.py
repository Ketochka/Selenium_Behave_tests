
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with vertical slider and two markers on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/slider/#range-vertical")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

@when('user prepares the bottom marker')    
def step_impl(context):
        slider = context.browser.find_element_by_xpath("//body/div[@id='slider-range']")
        height = slider.size['height']
        bottom_marker = context.browser.find_element_by_xpath("//body/div[@id='slider-range']/span[1]")
        actions = ActionChains(context.browser)
        actions.click_and_hold(bottom_marker).move_by_offset(0,-height).release().perform()
        time.sleep(1)
        
        
@when('user moves top marker and determines the upper value')    
def step_impl(context):
        slider = context.browser.find_element_by_xpath("//body/div[@id='slider-range']")
        height = slider.size['height']
        up_marker = context.browser.find_element_by_xpath("//body/div[@id='slider-range']/span[2]")
        actions = ActionChains(context.browser)
        actions.click_and_hold(up_marker).move_by_offset(0,height).release().perform()
        time.sleep(1)
        actions.click_and_hold(up_marker).move_by_offset(0,-height*0.85).release().perform()
        time.sleep(1)
        
@when('user moves bottom marker and determines the lower value')    
def step_impl(context):
        slider = context.browser.find_element_by_xpath("//body/div[@id='slider-range']")
        height = slider.size['height']
        bottom_marker = context.browser.find_element_by_xpath("//body/div[@id='slider-range']/span[1]")
        actions = ActionChains(context.browser)
        actions.click_and_hold(bottom_marker).move_by_offset(0,height).release().perform()
        time.sleep(1)
        actions.click_and_hold(bottom_marker).move_by_offset(0,-height*0.82).release().perform()
        time.sleep(1)              
        
@then('ensure price range is set correctly')    
def step_impl(context):    
        current = context.browser.find_element_by_xpath("//body/div[@id='slider-range']/div")
        current_value = current.get_attribute('style')
        print(current_value)
        assert(current_value == 'bottom: 82%; height: 3%;')

