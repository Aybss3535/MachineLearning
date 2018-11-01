# -*- coding=utf-8 -*-
from selenium import webdriver
import urllib
import time
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
# driver=webdriver.PhantomJS()
driver.get("https://www.baidu.com/")
# kw=driver.find_element_by_id('appCode')
img=driver.find_element_by_xpath("//div[@id='lg']/img[1]")
print(img.get_attribute("src"))
action=ActionChains(driver).move_to_element(img)
action.context_click(img)
action.send_keys(Keys.ARROW_DOWN)
time.sleep(3)
action.send_keys('v')
# news =driver.find_element_by_xpath("//div[@id='u1']/a[1]");
# action=ActionChains(driver).move_to_element(news)
# action.click(news)
action.perform()#**重要，只有写上这句才执行
# print(news)
# kw.send_keys("hello world")
# userName=driver.find_element_by_name("password")
# userName.send_keys("15860850321")

driver.close()
driver.quit()