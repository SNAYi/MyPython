#coding=utf-8
from selenium import webdriver
browser=webdriver.Firefox()
browser.get("http://www.baidu.com")
data=browser.find_element_by_id("cp").text
print data
browser.quit()