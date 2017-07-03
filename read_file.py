#读取文件并将文件准换成excel表格
# import json
# with open('/Users/jiangli/Documents/学习内容/github作业/homework/day-1/task-1','rt') as f1:
#     data = f1.read()
#     for line in f1:
#
#     print(data)
f1 = open("/Users/jiangli/Documents/学习内容/github作业/homework/day-1/courses.json")
line = f1.readline()
while line:
    print(line)
    line = f1.readline()
f1.close()
