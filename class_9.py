# 创建和使用类
# 9.1
# # This constructor takes no arguments这个构造函数没有参数
# class Dog:
# 	"""模拟小狗的动作"""
# 	# __init__左右两边各有两个下划线是一种约定，旨在避免默认方法与普通方法发生冲突
# 	# 初始化  self 可以理解为this关键字    
# 	def __init__(self,name,age):
# 		"""初始化name和age"""
# 		self.name = name
# 		self.age = age

# 	def sit(self):
# 		print(self.name.title()+"is now sitting.")

# 	def roll_over(self):
# 		print(self.name.title()+"is now rolled over.")

# my_dog = Dog("ellen",12)
# print("My dog name is :"+my_dog.name.title()+".")
# print("My dog age is :"+str(my_dog.age)+" years old.")
# 
# 
# 
# map可以包含一个函数和一个列表
# 假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，
# 把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
# def get_name(s):
# 	return s.title()
# print(map(get_name,['adam','LISA','barT']))
# 
# 
# 9.2  reduce和map参数类型相似，但是可以写多个参数
# def prod(x,y):
# 	return x*y
# print reduce(prod,[2,4,5,7,12])
# 
# 
# 9.3  函数的扩展  请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 第一种方法
# import math
# def ins_sqr(x):
# 	ins = math.sqrt(x)
# 	if int(ins) == ins:
# 		return x
# print filter(ins_sqr,range(1,101))
# 第二种方法  通过取余
# import math
# def is_sqr(x):
#     return math.sqrt(x)%1==0
# print filter(is_sqr, range(1, 101))
# 
# 
# 对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。

# 输入：['bob', 'about', 'Zoo', 'Credit']
# 输出：['about', 'bob', 'Credit', 'Zoo']
# def sorteds(s1,s2):
# 	return cmp(s1.lower(),s2.lower())
# print sorted(['bob', 'about', 'Zoo', 'Credit'],sorteds)
# 
# 
# 
# 9.10  format()通过对象属性  有问题
# <__main__.Person instance at 0x102ae8c20>解决办法：对返回的函数进行调用才能输出结果
# class Person:
#  	def __init__(self,name,age):
#  		self.name,self.age = name,age
#  		def __str__(self):
#  			return 'This guy is {self.name},is {self.age} old'.format(self=self)
# result = Person('kzc',18)
# print resule(str(('kzc',18))
# 
# 
# 9.11
# 请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
# def calc_prod(lst):
# 	for i in lst():
# 		for j in lst():
# 			list = i*j
# 			return list
# f = calc_prod([1,2,3,4])
# def calc_prod(lst):
# 	def prod():
# 		return reduce(lambda x,y:x*y,lst)
# 	return prod
# f = calc_prod([1,2,3,4])
# print f()

# from functools import reduce
# prodect = reduce(lambda x,y:x*y,[1,2,3,4])
# print prodect
# 
# 下面是class实例
# class Person:
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def work(self):
# 		print(self.name.title()+" is working now.")
# 	def roll_over(self):
# 		print(self.name.title()+" is rolled over now.")
# result = Person('guanwen',20)
# print("Your name is "+result.name.title()+".")
# print("Your age is "+str(result.age)+" years old.")
# print("He is "+str(result.roll_over())+".")
# d = {
# 	'Adam':95,
# 	'Lisa':85,
# 	'Bart':59
# }
# for  name,score in d.items():
# 	print "%s:%d" %(name,score)


