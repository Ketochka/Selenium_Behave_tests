
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with incremental slider on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/slider/#steps")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

    
@when('user mover marker to the right to set $150 as a value')    
def step_impl(context):
        slider = context.browser.find_element_by_xpath("//body/div[@id='slider']")
        width = slider.size['width']
        marker = context.browser.find_element_by_xpath("//body/div[@id='slider']/span")
        actions = ActionChains(context.browser)
        actions.click_and_hold(marker).move_by_offset(-width, 0).release().perform()
        time.sleep(1)
        actions.click_and_hold(marker).move_by_offset(width*0.3, 0).release().perform()

@then('ensure marker has the correct position')    
def step_impl(context):    
        marker = context.browser.find_element_by_xpath("//body/div[@id='slider']/span")
        marker_pos = marker.get_attribute('style')
        assert(marker_pos == 'left: 30%;')

