
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with vertical slider on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/slider/#slider-vertical")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

@when('user sets the value on vertical slider')    
def step_impl(context):
        slider = context.browser.find_element_by_xpath("//body/div[@id='slider-vertical']")
        height = slider.size['height']
        marker = context.browser.find_element_by_xpath("//body/div[@id='slider-vertical']/span")
        actions = ActionChains(context.browser)
        actions.click_and_hold(marker).move_by_offset(0,height).release().perform()
        time.sleep(1)
        actions.click_and_hold(marker).move_by_offset(0,-height*0.4).release().perform()
        time.sleep(1)
        
@then('ensure marker position is correct')    
def step_impl(context):    
        current = context.browser.find_element_by_xpath("//body/div[@id='slider-vertical']/span")
        current_value = current.get_attribute('style')
        assert(current_value == 'bottom: 40%;')

