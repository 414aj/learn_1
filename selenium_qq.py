#!python3

import sys,time
from selenium import webdriver

browser=webdriver.Firefox()
browser.get("https://mail.qq.com")
time.sleep(5)

browser.switch_to.frame("login_frame")
uElem=browser.find_element_by_name('u')
uElem.clear()
uElem.send_keys('2675849542')
pElem=browser.find_element_by_name('p')
pElem.clear()
pElem.send_keys('201314asdb')
browser.find_element_by_id("login_button").click()
time.sleep(5)

qElem=browser.find_element_by_link_text('退出')
browser.find_element_by_link_text('写信').click()
time.sleep(5)
browser.switch_to.frame('mainFrame')
aElem=browser.find_element_by_id("toAreaCtrl")
aElem.send_keys('aj_is_me@qq.com')
bElem=browser.find_element_by_id('subject')
bElem.send_keys('xxxx')

frame=browser.find_element_by_xpath("//*[@id='QMEditorArea']/table/tbody/tr/td/iframe")
browser.switch_to.frame(frame)
cElem=browser.find_element_by_xpath('/html/body')
cElem.send_keys("xxxxxxxxx")
#time.sleep(2)
browser.switch_to.parent_frame()
browser.find_element_by_link_text('发送').click()
time.sleep(5)
qElem.click()
browser.close()