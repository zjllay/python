from selenium import webdriver
import time
import requests
import bs4
def getback():
    driver = webdriver.Firefox()
    # 访问百度首页
    first_url = 'http://www.baidu.com'
    print('now access %s' %(first_url))
    driver.get(first_url)
    time.sleep(3)
    # 访问新闻页面
    second_url = 'http://www.wanmen.org/#/'

    print('now access %s' %(second_url))
    driver.get(second_url)
    time.sleep(3)
    # 返回（后退）到百度首页
    print('back to %s' %(first_url))
    driver.back()
    time.sleep(3)
    #  前进到新闻页
    print('forward to %s' %(second_url))
    driver.forward()
    time.sleep(10)

    driver.quit()
def readhtml():
    response = requests.get('http://www.wanmen.org/#/')
    # 打印当前网页元素
    print('now read html is %s' %(response.text))
    # 打印出当前的编码
    print(response.encoding)
    #打印出类型
    print(type(response.text))
    # 打印当前的编码类型
    print(response.apparent_encoding)
def openhtml():
    response = requests.get('http://www.wanmen.org/#/course/58be80302f4e7cd4de1086bd')
    soup = bs4.BeautifulSoup(response.text)
    return [a.attrs.get('href') for a in soup.select()]
