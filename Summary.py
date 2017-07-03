#python入门知识汇总
print('=========1 用zip将两个列表改成字典=================')
keys = ['a','b','c','d','e']
values = ['2','5','25','1','12']
for key,value in zip(keys,values):
    print(key+':'+value)

print('-------普通的字典没有顺序----------------')
message = {
	'first_name'  : 'alien',
	'age' : '14',
	'city' :'beijing'
}
for k,v in message.items():
    print(k+':'+v)

print('-------方法1，计算两数的和----------------')
def add(a,b):
    print(a+b)
add(4,6)
def add1(a=1,b=4):
    return a+b
print(add1())
print('========class and method===================')
class A():
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def add(self):
        return self.a + self.b
    def product(self):
        return self.a * self.b
count = A('3',7)
print(count.add())
print(count.product())

print('=============inherit========================')
class A():
    def add(self,a,b):
        return a + b
class B(A):
    def sub(self,a,b):
        return a - b
print(B().add(4,5))
