def getDemo():
    with open('/Users/jiangli/Documents/学习内容/username') as file_obj:
        contents = file_obj.read()
        print(contents)
getDemo()
