# python抓取网页资源的N种方法
import urllib.request
# response = urllib.request.urlopen('http://python.org/')
# html = response.read()
#
req = urllib.request.Request('http://baidu.com/')
response = urllib.request.urlopen(req)
the_page = response.read()
print(the_page)
#
# cs_url = 'http://www.so.com/s'
# param  = {'ie':'utf-8', 'q':'query'}
#
# r = urllib.request.urlopen(cs_url, params = param)
# print(r.url)
