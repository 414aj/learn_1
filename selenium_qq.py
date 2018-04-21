#!python3
#使用selenium模拟登陆qq邮箱并发送邮件
#目前能正常登陆邮箱
#写邮件时，邮件内容无法发送到正文内容区域，而是发送到了收件人输入框里

import sys,time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser=webdriver.Firefox()
browser.get("https://mail.qq.com")
time.sleep(5) #等待页面加载完成

browser.switch_to.frame("login_frame") #跳转到login_frame
browser.find_element_by_xpath("/html/body/div/div/div/a[2]").click() #使用账户和密码登陆
uElem=browser.find_element_by_name('u') #依次发送账号和密码，并点击登陆
uElem.clear()
uElem.send_keys('xxxxxxxxxxxxx')
pElem=browser.find_element_by_name('p')
pElem.clear()
pElem.send_keys('xxxxxxxxxxxxx')
browser.find_element_by_id("login_button").click()
time.sleep(5) #等待页面加载完成

browser.switch_to.default_content() #跳转到主界面
browser.find_element_by_link_text('写信').click() #点击写信按键
time.sleep(5) #等待页面加载完成

browser.switch_to.frame('mainFrame') #跳转到mainFrame
aElem=browser.find_element_by_xpath("//*[@id='toAreaCtrl']/div[2]/input") #定位收件人
aElem.send_keys('xxxxxxxxxxxxx') #发送收件人邮箱
     
frame=browser.find_element_by_xpath("//*[@id='QMEditorArea']/table/tbody/tr/td/iframe") #定位邮件正文的frame
browser.switch_to.frame(frame) #跳转到frame
cElem=browser.find_element_by_xpath('/html/body') #定位邮件正文内容区域
cElem.send_keys("xxxxxxxxx") #发送邮件正文

browser.switch_to.parent_frame() #回到mainFrame
browser.find_element_by_link_text('发送').click() #点击发送邮件
time.sleep(5) #等待页面加载
browser.close() #关闭browser