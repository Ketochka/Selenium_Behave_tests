
# coding: utf-8

# In[9]:

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with horizontal slider on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/slider/#default")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

    
@when('user moves slider by 410 points to the right')    
def step_impl(context):
        slider = context.browser.find_element_by_xpath("//body/div[@id='slider']/span")
        actions = ActionChains(context.browser)
        actions.drag_and_drop_by_offset(slider,410,0)
        actions.perform()

@then('ensure slider position is changed correctly')    
def step_impl(context):    
        slider = context.browser.find_element_by_xpath("//div[@id='slider']/span")
        slider_location_after=slider.location
        x2=slider_location_after.get('x')
        assert(x2>=410)
        

