import pymongo
import pprint
import requests
import m3u8


# 连接数据库[父类]
class Conn():
# 拿到数据库连接
    def getConnection(self):
    # 连接主机
        conn = pymongo.MongoClient('10.8.8.8',27017)
        return conn
    # 连接数据库  存储到数据库中
    def saveToDB(self):
        conne = self.getConnection()
        db = conne.allus
        status_code_m3u8 = db.get_collection('status_code_m3u8')
        everything = db.videos.find()

        error_m3u8 = []
        error_ts = []
        for h in everything:
            hls = h['hls']
            # s = ''.join(h['name'])字符串的拼接
            for status in hls:
            #判断m3u8视频文件是否正常
                r = requests.head('http://media.wanmen.org/')
                # print(r.status_code)
                # print(h['name'])
                if r.status_code == 200:
                    print('m3u8视频OK')
                    # for ts in r.selements:
                    #     if ts.status_code == 200:
                    #         print('ts文件正常')
                    #     else:
                    #         print(error_ts.append(r.selements))
                    #         print(h['name'])
                else:
                    print(hls)
                    print(h['name'])
                    print(r.status_code)

                    document = {}
                    document['_id'] = videos['_id']
                    document['videoId'] = videos['videoId']
                    document['name'] = videos['name']
                    document['hls'] = videos[hls][key]
                    document['status_code'] = r.status_code
                    db.status_code_m3u8.insert(document)


                # print(error_m3u8.append(r))
                # print(h['name'])
                # print(hls)
                # for ts in r.selements:
                #     if ts.status_code == 200:
                #         print('ts文件正常')
                #     else:
                #         print(error_ts.append(r.selements))
                #         print(h['name'])
