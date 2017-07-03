import requests
import json
from bs4 import BeautifulSoup
def reads():
    # 读取数据
    response = requests.get('http://www.baidu.com/')
    html = BeautifulSoup(response.text)
    # 枚举的使用  获取图片
    for index,each in enumerate(html.select('img')):
        with open('{}.jpg.format(index)','wb') as jpg:
            jpg.write(requests.get(each.attrs['src'],stream = True).content)

def status():
    response = requests.get('http://www.baidu.com/')
    res = response.status_code
    print('status is:'+str(res))
    print('======2======')
    res1 = response.headers['content-type']
    print(res1)
    print('=====3========')
    print(response.encoding)
    print('=======4========')
    print(response.text)
    print('======5========')
    print(response.json)
    print('=========6==========')
    print(response.url)

def test():
    res = requests.get('http://www.wanmen.org/#/live/58f71587895b5842cbd69908')
    print(res.status_code)

def getSession():
    s = requests.Session()
    # s.get('https://www.baidu.com/')
    r = s.get("https://www.baidu.com/")
    print(r.text)
reads()
