
# coding: utf-8

# In[3]:

from behave import *
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('page with two date select blocks')
def step_impl(context):
        context.browser.get("http://jqueryui.com/datepicker/#date-range")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)
        
@when('user selects from date')    
def step_impl(context):
        datepicker_from = context.browser.find_element_by_xpath("//input[@id='from']")
        datepicker_from.click()
        wait = WebDriverWait(context.browser, 10)
        month_from = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@class='ui-datepicker-month']")))
        select_month_from = Select(month_from)
        select_month_from.select_by_visible_text("Jun")
        wait = WebDriverWait(context.browser, 10)
        date_from = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td/a[text()='17']")))
        date_from.click()

@when('user selects to date')    
def step_impl(context):        
        datepicker_to = context.browser.find_element_by_xpath("//input[@id='to']")
        datepicker_to.click()
        month_to = context.browser.find_element_by_xpath("//select[@class='ui-datepicker-month']")
        select_month_to = Select(month_to)
        select_month_to.select_by_visible_text("Aug")
        wait = WebDriverWait(context.browser, 10)
        date_to = wait.until(EC.presence_of_element_located((By.XPATH, "//tbody/tr/td/a[text()='31']")))
        date_to.click()

@then('date range becomes determined')    
def step_impl(context):  
        datepicker_from = context.browser.find_element_by_xpath("//input[@id='from']")
        value_from = datepicker_from.get_attribute('value')
        datepicker_to = context.browser.find_element_by_xpath("//input[@id='to']")
        value_to = datepicker_to.get_attribute('value')
        assert(value_from == '06/17/2016')
        assert(value_to == '08/31/2016')
        
