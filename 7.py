# Chapter 7
#the first example(input text)
# message = input("Please tell me something,and I will repeat it back to you:")
# print(message)
# 
# 
# The second example()
# promt = "If you tell us who you are,we can personalize the message you see."
# promt += "\nwhat is your first name?\n"
# name = input(promt)
# print name
# 
# 
# The third example(int())
# province = "How many provinces in China?"
# provinces = input(province)
# provinces = int(provinces)
# if provinces >= 10:
# 	print "correct answer"
# else:
# 	print "wrong ansert!"
# 	
# 	
# 	4 exercise
# num = input("Please enter a number:")
# num = int(num)
# if num %10 == 0:
#  	print(str(num)+" is a multiple of ten")
# else:
# 	print("Sorry "+str(num)+" is not a multiple of ten")
# 	
# 	5 example  while
prompt = "\n Tell me something,and I will repeat it back to you!"
prompt += "\nEnter 'quit' to end the program!\n"
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)

