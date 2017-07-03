import requests

class Open():
    def OpenTest():
        try:
            fh = open('/Users/jiangli/Documents/学习内容/testfile','w')
            fh.write('这是一个测试文件，检查异常!')
        except IOError:
            print('Error:没有找到该文件或者读取文件失败')
        else:
            print('内容写入文件成功')
            fh.close()
# class Req():
#     def __init__(self):
#         # 读取数据
#         response = requests.get('http://www.baidu.com/')
#         # 判断状态码是否是200  OK
#         print(response.status_code())


# def combine(source, maxsize):
#     parts = []
#     size = 0
#     for part in source:
#         parts.append(part)
#         size += len(part)
#         if size > maxsize:
#             yield ''.join(parts)
#             parts = []
#             size = 0
#         yield ''.join(parts)
#
# # 结合文件操作
# with open('filename', 'w') as f:
#     for part in combine(sample(), 32768):
#         f.write(part)
