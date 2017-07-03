import json
def tryE():
    print('Give me two number,I will divide them!')
    print("Enter 'q' to quit")

    while True:
        first_name = input('the first name:\n')
        if first_name == 'q':
            break
        last_name = input('the last name:\n')
        if last_name == 'q':
            break
        try:
            answer = int(first_name)/int(last_name)
        except:
            print('error')
        else:
            print(answer)
def count_words():
    filename = '/Users/jiangli/Documents/学习内容/testfile'
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        print('File Not Found!')
    # 计算文档中有多少字符
    words = content.split()
    # 调用split()以生成一个列表
    num = len(words)
    print(filename+' file have '+str(num)+' String!')
    # have some error
def json():
    numbers = [1,2,3,4,5,0]
    filename = 'numbers.json'
    with open(filename,'w') as f_json:
        json.dump(numbers,f_json)
def reader():
    filename = 'numbers.json'
    with open(filename) as f_obj:
        numbers = json.load(f_obj)
        print(numbers)
reader()
