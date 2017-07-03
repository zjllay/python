import pymongo
import requests
# 1、连接数据库
conn = pymongo.MongoClient('10.8.8.8',27017)
db = conn.allus
# 2、检查m3u8视频是否正常
check1 = db.get_collection('check1')
check1_null = db.get_collection('check_null')
num = 0
for h in db.videos.find({}):
    hls = h['hls']
    num = num+1
    print(num)
    print(h['name'])

    try:
        for key in hls:
            res = requests.head(hls[key])
            # print(res.status_code)
            if hls[key] != None:
                if res.status_code == 404:
                    error_m3u8 = {}
                    error_m3u8['_id'] = h['_id']
                    error_m3u8['name'] = h['name']
                    error_m3u8['hls'] = hls[key]
                    error_m3u8['status_code'] = res.status_code

                    check1.insert(error_m3u8)

            elif hls[key] == None:
                # 可以输出error
                checkNull = {}
                checkNull['_id'] = h['_id']
                checkNull['name'] = h['name']
                checkNull['hls'] = null

                check1_null.insert(checkNull)
    except:
        print('Exception!')
