
# coding: utf-8

# In[10]:

from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@given('page with multiple sliders on it')
def step_impl(context):
        context.browser.get("http://jqueryui.com/slider/#multiple-vertical")
        wait = WebDriverWait(context.browser, 10)
        frame_ = wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
        context.browser.switch_to_frame(frame_)
        
@when('user increases the volume and makes EQ shape to be concave')    
def step_impl(context):
        volume_main = context.browser.find_element_by_xpath("//body/div[@id='master']")
        volume_current = context.browser.find_element_by_xpath("//body/div[@id='master']/div")
        volume_marker = context.browser.find_element_by_xpath("//body/div[@id='master']/span")
        eq1_current = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[1]/div")
        eq1_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[1]/span")
        eq7_current = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[7]/div")
        eq7_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[7]/span")
        eq4_current = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[4]/div")
        eq4_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[4]/span")
        width = volume_main.size['width']
        width_current = volume_current.size['width']
        to_max = width - width_current
        actions = ActionChains(context.browser)
        actions.click_and_hold(volume_marker).move_by_offset(to_max, 0).release().perform()
        actions.click_and_hold(eq1_marker).move_by_offset(0, -(120 - eq1_current.size['height'])).release().perform()
        actions.click_and_hold(eq7_marker).move_by_offset(0, -(120 - eq7_current.size['height'])).release().perform()
        actions.click_and_hold(eq4_marker).move_by_offset(0, -(30 - eq4_current.size['height'])).release().perform()
        
        

@when('user continues making EQ shape to be concave')    
def step_impl(context):
        eq2_current = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[2]/div")
        eq2_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[2]/span")
        eq3_current = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[3]/div")
        eq3_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[3]/span")
        
        eq5_current = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[5]/div")
        eq5_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[5]/span")
        eq6_current = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[6]/div")
        eq6_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[6]/span")
        
        move2 = eq2_current.size['height']-90
        move3 = eq3_current.size['height']-60
        move5 = eq5_current.size['height']-60
        actions = ActionChains(context.browser)
        actions.click_and_hold(eq2_marker).move_by_offset(0, move2).release().perform()
        actions.click_and_hold(eq6_marker).move_by_offset(0, -10).release().perform()
        actions.click_and_hold(eq3_marker).move_by_offset(0, move3).release().perform()
        actions.click_and_hold(eq5_marker).move_by_offset(0, move5).release().perform()
        time.sleep(.5)
        
@when('user lowers the volume and makes EQ shape to be convex')    
def step_impl(context):
        volume_main = context.browser.find_element_by_xpath("//body/div[@id='master']")
        volume_marker = context.browser.find_element_by_xpath("//body/div[@id='master']/span")
        volume_current = context.browser.find_element_by_xpath("//body/div[@id='master']/div")
     
        eq1_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[1]/span")
        eq4_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[4]/span")
        eq7_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[7]/span")
        
        width = volume_main.size['width']
        width_current = volume_current.size['width']
        
        actions = ActionChains(context.browser)
        actions.click_and_hold(volume_marker).move_by_offset(-width, 0).release().perform()
        actions.click_and_hold(eq1_marker).move_by_offset(0,120).release().perform()
        actions.click_and_hold(eq7_marker).move_by_offset(0,120).release().perform()
        actions.click_and_hold(eq4_marker).move_by_offset(0, -90).release().perform()   
        
        
@when('user continues making EQ shape to be convex')    
def step_impl(context):
        eq2_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[2]/span")
        eq6_marker = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[6]/span")
        actions = ActionChains(context.browser)
        actions.click_and_hold(eq2_marker).move_by_offset(0, 30).release().perform()
        actions.click_and_hold(eq6_marker).move_by_offset(0, 60).release().perform()
        time.sleep(5)

            
@then('ensure there is actual mute')    
def step_impl(context):         
        volume_current = context.browser.find_element_by_xpath("//body/div[@id='master']/div")
        eq1_current = context.browser.find_element_by_xpath("//body/div[@id='eq']/span[1]/div")
        ismute = volume_current.get_attribute('style')
        is_1 = eq1_current.get_attribute('style')
        assert(ismute=='width: 0%;')
        assert(is_1=='height: 0%;')
        
        

