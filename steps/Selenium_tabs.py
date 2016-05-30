
# coding: utf-8

# In[19]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('page with three tabs on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/tabs/")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)
        
    
@when('user clicks on the second and then on the third tab')    
def step_impl(context):
        tab2 = context.browser.find_element_by_xpath("//div[@id='tabs']/ul/li[@aria-controls='tabs-2']")
        tab2.click()
        time.sleep(2)
        is_tab2_expanded = tab2.get_attribute('aria-expanded')
        assert(is_tab2_expanded == 'true')


@then('second and third tab are displayed respectively')    
def step_impl(context):  
        wait = WebDriverWait(context.browser, 10)
        tab3 = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='tabs']/ul/li[@aria-controls='tabs-3']")))
        tab3.click()
        is_tab3_expanded = tab3.get_attribute('aria-expanded')
        assert(is_tab3_expanded == 'true')
    

