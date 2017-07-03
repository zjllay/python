import pymongo
import requests
import pprint
# 连接数据库
conn = pymongo.MongoClient('10.8.8.8',27017)
db = conn.allus['courses']
# print(db)
# pictures = db.getCollection('courses').find({bigImage:{$not:/imgs/}},{_id:0,name:1}).sort({$natural:-1})
# for name in pictures:
#     print(name)
# $ne   is not equals  查询所有不等于imgs的数据
find_select1 = db.count({'bigImage': { '$ne': '/imgs/' }})
print(find_select1)
# find_select2 = db.getCollection('courses').find( { bigImage: { $not: /imgs/ } })
# find_select2  = db.count( {'bigImage' : '{ $regex : /img/ }' })
# print(find_select2)
find_select3 = db.users.find({}).count()
print(find_select3)
# for data in find_select2:
#     pprint.pprint(data)
#     print('======================================')

conn.close()
