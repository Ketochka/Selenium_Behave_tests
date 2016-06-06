
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with colorpicker on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/slider/#colorpicker")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)
        
@when('user sets 216 on red channel')    
def step_impl(context):
        red = context.browser.find_element_by_xpath("//body/div[@id='red']/span")
        red_main = context.browser.find_element_by_xpath("//body/div[@id='red']/div")
        width = red_main.size['width']
        print(width)
        actions = ActionChains(context.browser)
        actions.click_and_hold(red).move_by_offset(-300, 0).release().perform()
        time.sleep(.5)
        actions.click_and_hold(red).move_by_offset(217/255 * width, 0).release().perform()
        time.sleep(.5)
        
@when('user sets 81 on green channel')    
def step_impl(context):
        green = context.browser.find_element_by_xpath("//body/div[@id='green']/span")
        width = 300 
        actions = ActionChains(context.browser)
        actions.click_and_hold(green).move_by_offset(-300, 0).release().perform()
        time.sleep(.5)
        actions.click_and_hold(green).move_by_offset(81/255 * width, 0).release().perform()
        time.sleep(.5)    
        
@when('user sets 41 on blue channel')    
def step_impl(context):
        blue = context.browser.find_element_by_xpath("//body/div[@id='blue']/span")
        width = 300        
        actions = ActionChains(context.browser)
        actions.click_and_hold(blue).move_by_offset(-300, 0).release().perform()
        time.sleep(.5)
        actions.click_and_hold(blue).move_by_offset(41/255 * width, 0).release().perform()
        time.sleep(5)          

@then('ensure RGB value is set correctly')    
def step_impl(context):         
        swatch = context.browser.find_element_by_xpath("//body/div[@id='swatch']")
        color = swatch.get_attribute('style')
        print(color)
        assert(color=='background-color: rgb(216, 81, 41);')
        

