# name = {
# 	'alien':'ruby',
# 	'sarah':'java',
# 	'phil':'python',
# 	'lisa':'java'
# }
# # print 'lisa favorite language is: '+name['lisa'].title()+'.'
# message = {
# 	'first_name'  : 'alien',
# 	'age' : '14',
# 	'city' :'beijing'
# }
# for name1 in name.items():
	# print name1
# print str(message['first_name'])+' de age is: '+str(message['age'])+'\ncity is:'+str(message['city'])
# for key,value in message.items():
# 	print("\nValue:"+str(value))
# 	print("Key:"+str(key))
# for name1 in name.keys():
# 	print(name1.title())
# 	keys() values() lists()
# friend = ['phil','lisa']
# for name1 in sorted(name.values()):
# 	print name1.title()

# 	if name1 in friend:
# 		print 'Hi\t'+name1.title()+",I see your favorite language is:\t"+name[name1].title()+"!"
# aliens = []
# for alien_number in range(30):
# 	new_alien = {'color':'red','speed':50}
# 	aliens.append(new_alien)
# for num in aliens[:5]:
# 	print(num)
# print("...")
# print("Total numbers of aliens :"+str(len(aliens)))
# 	new_alien={'color':'red','age':'23'}
# 	aliens.append(new_alien)

# for alien in aliens[:5]:
# 	print(alien)
# print("...")
# print("Total number of aliens:"+str(len(aliens)))
 
# 5\modify
# robet = []
# for orige in range(0,30):
# 	new_robet = {'color':'red','speed':'low','points':5}
# 	robet.append(new_robet)
# for num in robet[0:5]:
# 	if num['color'] == 'red':
# 		num['color'] = 'gree'
# 		num['speed'] = 'medium'
# 		num['points'] = 15
# 	print num
# print("...")
# 
#6\storiage
# for topping1 in pizza['topping']:
# 	print("\t"+topping1)
# pizza = {
# 	'crust' : 'tick',
# 	'topping' : ['mushrooms','extra cheese']
# }
# print("you ordered a "+pizza['crust']+"-crust pizza" +"with the follwing toppings:")
# for topp in pizza['topping']:
# 	print topp
# 	
# 	7\list
# favorite = {
# 	'jen' : ['python','ruby'],
# 	'edward' : ['c'],
# 	'sarah' : ['go','ruby'],
# 	'phil' : ['java','haskell']
# }

# for name,languages in favorite.items():
# 	print(name.title()+" is favorite languages are:")
# 	for language in languages:
# 		print("\t"+language.title())
# 8\storigr list
user = {
	'lisa' : {
		'first' : 'albelt',
		'last' : 'lisa',
		'location' : 'princeton'
	},
	'allen' :{
		'first' : 'marie',
		'last' : 'cruie',
		'location' : 'paris'
	}

}
for name,info in user.items():
	print("Username: "+info['first'].title()+" "+info['last'].title())
	print("location is: "+info['location']+"\n")