import pymongo
import requests
def saveDB():
    # 1、连接主机 connection host
    conn = pymongo.MongoClient('10.8.8.8',27017)
    # 2、连接数据库  connection db
    db = conn.allus
    # 3、建立集合
    error_m3u8 = db.get_collection('error_m3u8')
    # 4、遍历表中的数据
    everything = db.videos.find()
    num = 0
    for hls in everything:
        # 遍历表中hls的key值
        h = hls['hls']
        print(h)
        print(hls['name'])
        num += 1
        print(num)
        try:
            for key in h:
                res = requests.head(h[key])
                print(res)
        except ConnectionError:
            print('Excepttion')
ppri = saveDB()
ppri
