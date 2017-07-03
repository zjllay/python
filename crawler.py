# # 关于网站的爬虫
import requests
import time
import urllib
from multiprocessing import Queue
from selenium import webdriver

# 1、打开网页(爬取图片)
driver = webdriver.Firefox()
# driver.get('https://accounts.ctrip.com/member/login.aspx')
driver.get('http://www.wanmen.org/#/course/586d23485f07127674135d40?lecture=586d23535f071276741590f6')
time.sleep(3)
driver.refresh()
time.sleep(20)
driver.quit()
