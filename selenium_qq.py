#!python3

import sys,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Firefox()
browser.get("https://mail.qq.com")
time.sleep(5)

browser.switch_to.frame("login_frame")
browser.find_element_by_xpath("/html/body/div/div/div/a[2]").click()
uElem=browser.find_element_by_name('u')
uElem.clear()
uElem.send_keys('2675849542')
pElem=browser.find_element_by_name('p')
pElem.clear()
pElem.send_keys('201314asdb')
browser.find_element_by_id("login_button").click()
time.sleep(5)

browser.switch_to.default_content()
browser.find_element_by_link_text('写信').click()
time.sleep(5)
browser.switch_to.frame('mainFrame')
aElem=browser.find_element_by_xpath("//*[@id='toAreaCtrl']/div[2]/input")
aElem.send_keys('aj_is_me@qq.com')

frame=browser.find_element_by_xpath("//*[@id='QMEditorArea']/table/tbody/tr/td/iframe")
browser.switch_to.frame(frame)
cElem=browser.find_element_by_xpath('/html/body')
cElem.send_keys("xxxxxxxxx")

browser.switch_to.parent_frame()
browser.find_element_by_link_text('发送').click()
time.sleep(5)
browser.close()