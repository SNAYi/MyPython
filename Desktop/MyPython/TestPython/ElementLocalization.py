#coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
time.sleep(1)
browser.get("http://www.baidu.com")
time.sleep(1)
browser.find_element_by_class_name("s_ipt").send_keys("CSDN")
time.sleep(1)
browser.find_element_by_id("su").click()
browser.quit()









