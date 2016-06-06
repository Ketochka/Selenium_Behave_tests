
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with scroller and 20 numbers on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/slider/#side-scroll")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)

    
@when('user scrolls to the right and makes number 17 visible')    
def step_impl(context):
        scroller = context.browser.find_element_by_xpath("//body/div[contains(@class,'scroll-pane')]")
        width = scroller.size['width']
        scrollbar = context.browser.find_element_by_xpath("//div[@class='ui-handle-helper-parent']")
        time.sleep(1)
        actions = ActionChains(context.browser)
        actions.click_and_hold(scrollbar).move_by_offset(width/20*17, 0).release().perform()
        time.sleep(1)

@then('ensure number 17 is visible')    
def step_impl(context):    
        number_17 = context.browser.find_element_by_xpath("//div[@class='scroll-content']/div[17]")
        assert(number_17.is_displayed())

