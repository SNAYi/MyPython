#coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Firefox()
browser.get("http://www.baidu.com")
print browser.title
print browser.current_url
browser.quit()