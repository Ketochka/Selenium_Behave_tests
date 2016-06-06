
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with horizontal slider with dropdown')
def step_impl(context):
        context.browser.get("http://jqueryui.com/slider/#hotelrooms")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

    
@when('user selects the desired number of beds equal to 5')    
def step_impl(context):
        dropdown = context.browser.find_element_by_xpath("//select[@id='minbeds']")
        dropdown.click()
        dropdown_option = context.browser.find_element_by_xpath("//form[@id='reservation']/select[@id='minbeds']/option[text()='5']")
        dropdown_option.click()
        time.sleep(1)
        current = context.browser.find_element_by_xpath("//div[@id='slider']/div")
        result = current.get_attribute('style')
        assert(result=='width: 80%;')
        time.sleep(1)

@when('user selects the desired number of beds equal to 1')    
def step_impl(context):
        dropdown = context.browser.find_element_by_xpath("//select[@id='minbeds']")
        dropdown.click()
        dropdown_option = context.browser.find_element_by_xpath("//form[@id='reservation']/select[@id='minbeds']/option[text()='1']")
        dropdown_option.click()
        time.sleep(1)
        current = context.browser.find_element_by_xpath("//div[@id='slider']/div")
        result = current.get_attribute('style')
   

@then('1 bed is a selected option')    
def step_impl(context):    
        current = context.browser.find_element_by_xpath("//div[@id='slider']/div")
        result = current.get_attribute('style')
        assert(result=='width: 0%;')

