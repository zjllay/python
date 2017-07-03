from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://www.126.com/')
print("=============Before login===========")
# 打印当前页面的title
title = driver.title
print(title)
# 打印当前页面的URL
now_url1 = driver.current_url
print(now_url1)
# 执行邮箱登陆
try:
    driver.find_element_by_xpath("//input[@id='auto-id-1497509323495']").clear()
    # driver.find_element_by_class_name('j-inputtext dlemail').send_keys('jsprza76520@26.com')
except:
    print('error')
# driver.find_element_by_class_name('j-inputtext dlemail').send_keys('username')
# driver.find_element_by_id('auto-id-1497508006267').clear()
# driver.find_element_by_class_name('j-inputtext dlpwd').send_keys('password')
# driver.find_element_by_id('dologin').click()

# print('===========After login============')
# # 再次打印当前页面的title
# title = driver.title
# print(title)
#
# # 打印当前页面的URL
# now_url2 = driver.current_url()
# print(now_url2)
# # 获取登陆的用户名
# user = driver.find_element_by_class_name('j-inputtext dlemail').text()
# print(user)

time.sleep(8)
driver.quit()







# from multiprocessing import Queue
# initial_page = "http://www.renminribao.com"
# url_queue = Queue()
# seen = set()
# seen.insert(initial_page)
# url_queue.put(initial_page)
#
# while(True): #一直进行直到海枯石烂
#     if url_queue.size()>0:
#         current_url = url_queue.get()    #拿出队例中第一个的url
#         store(current_url)               #把这个url代表的网页存储好
#         for next_url in extract_urls(current_url): #提取把这个url里链向的url
#             if next_url not in seen:
#                 seen.put(next_url)
#                 url_queue.put(next_url)
#     else:
#         break


# import unittest
# import os
# import time
# from selenium import webdriver
# #coding=utf-8
# def click():
#     from selenium.webdriver.common.keys import Keys
#     driver = webdriver.Firefox()
#     driver.get("http://www.baidu.com")
#     driver.find_element_by_id("kw").send_keys(u"selenium2")
#     time.sleep(2)
#     driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)
#     time.sleep(3)
#     driver.find_element_by_id("kw").send_keys(Keys.SPACE)
#     driver.find_element_by_id("kw").send_keys(u"python")
#     time.sleep(2)
#     driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
#     time.sleep(3)
#     driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'x')
#     time.sleep(2)
#     driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'v')
#     time.sleep(3)
#     driver.find_element_by_id("su").send_keys(Keys.ENTER)
#     time.sleep(4)
#     driver.quit()
#
# driver = webdriver.Firefox()
# driver.get('http://www.wanmen.org/#/')
# # print('设置浏览器的宽480，高800显示')
# # driver.set_window_size(600,600)
# # 获得输入框的尺寸  .size
# elem = driver.find_element_by_id('js-account-input-field').send_keys('15826861440')
# elem = driver.find_element_by_name('password').send_keys('1111111111n')
# elem = driver.find_element_by_class_name('login-btn').click()
# print(size)
# ActionChains(driver).move_to_element(elem).perform()
# try:
#     driver.find_element_by_id('translateType').send_keys('hello')
#     driver.find_element_by_id('translateType').submit()
#     # driver.find_element_by_class_name('login-btn').click()
#     # # driver.find_element_by_id('js-account-input-field').send_keys('account')
#     # # driver.find_element_by_name('password').clear()
#     # # driver.find_element_by_name('password').send_keys('password')
#     # driver.find_element_by_class_name('registration-btn').click()
# except:
#     print('error')
# driver.quit()

# 进行代码成功执行的测试方法
# class PythonOrgSearch(unittest.TestCase):
#
#     def setUp(self):
#         driver = webdriver.Firefox()
#
#         driver.get("http://www.baidu.com/")
#         driver.assertIn("百度一下，你就知道", self.driver.title)
#         elem = driver.find_element_by_id("kw")
#         time.sleep(3)
#         elem.send_keys("selenium")
#         elem.send_keys(Keys.RETURN)
#         time.sleep(5)
#         driver.assertIn('百度一下，你就知道',t.title())
#         time.sleep(10)
#         driver.quit()
#
# if __name__ == "__main__":
#     unittest.main()
# driver.get('http://www.baidu.com/')
# assert '百度' in driver.title
# elem = driver.find_element_by_name('wd')
# elem.send_keys('Eastmount')
# elem.click('submit')
#
# # elem.send_keys(Keys.RETURE)
# assert '谷歌' in driver.title
# driver.save_screenshot('baidu.png')
# driver.close()
# driver.quit()

# def sele_01():
#     try:
#
#         driver = webdriver.Firefox()
#         driver.get('http://www.baidu.com')
#
#         driver.find_element_by_id('kw').send_keys('Selenium2')
#         # driver.find_element_by_class_name('s_ipt')
#         # driver.find_element_by_name('wd')
#         driver.find_element_by_id('su').click()
#         time.sleep(3)
#         # driver.quit()
#     except Exception:
#         print('error!')
# def sele_02():
#     try:
#         driver = webdriver.Firefox()
#         driver.get('http://www.youdao.com/')
#         driver.find_element_by_id('query').send_keys('hello')
#         # 提交输入框的内容
#         driver.find_element_by_id('query').submit()
#         driver.quit()
#     except Exception:
#         print('error!')
# sele_02()
