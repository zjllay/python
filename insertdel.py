name = []
print "I'd like to invite three of you to the party:"
name.append("tree")
name.append("flower")
name.append("water")
print name
print "But one of the guests was unable to attend"
name.insert(1,"red")
print name
del name[2]
print name 



name = []
name.append('allen')
name.append('bus')
name.append('sky')
print name
name.insert(2,'apple')
print name
del name[3]
print name
name.pop()
print name
name.append('zhaji')
name.append('babbab')
name.append('huaxinag')
print name 
name.pop(3)
print name
name.sort()
print name
name.sort(reverse = True)
print name

print "Here is the original list:"
print name
print "Here is the sorted list:"
print sorted(name)
print "Here is the original list:"
print name
# print name.reverse()
print name 
print len(name)
print name[-1]
print len(name)
print sorted(name)
print name 
name.sort(reverse = True)
print name
name.reverse()
print name

magicians = ['alice','david','carolina']
for magic in magicians:
	print magic.title()+",that is a good  trick"
for x in range(1,6):
	print x

number = list(range(1,11))
print number
number = []
for num in range(2,10,2):
	print num
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print squares

# for index in range(1,21):
	 # print index
# indexs = list(range(1,1000000))
# print indexs
digits = [1,2,3,4,5,6]
print min(digits)
print max(digits)
print sum(digits)

num1 = range(1,20,2)
for num2 in num1:
	print num2
num = list(range(3,31))
for num in num:
	if num%3 == 0:
		print num
	else:
		continue
name = ['cat','dog','tree','flower','deng']
print name[1:2]




