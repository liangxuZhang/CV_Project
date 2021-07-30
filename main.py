import json
import requests
import cv2
import time
import datetime
from matplotlib import pyplot as plt
import pymysql
import detect
import os

host = '172.16.127.18'
user = 'xz_user'
password = 'Xz@zaoz2021'
port = '3306'

def run():
    url = "http://60.214.100.134:10001/artemis-web/debug/"
    path_unhanded = 'unhanded/100121/'
    path_handed = 'ai-dispose/100121/'
    dict = {
            "appKey": "23189490",
            "appSecret": "k0CzWXJUOBH0yMlq9D31",
            "contentType": "application/x-www-form-urlencoded;charset=UTF-8",
            "headers": "{}",
            "httpMethod": "GET",
            "mock": "false",
            "parameter": "{}",
            "path": "/api/mss/v1/hls/37046803001310516439",
            "query": "{}"
            }
    i = 0
    req1 = requests.post(url, dict)
    jsession1 = json.loads(req1.text)
    nurl = jsession1['data'].replace("10.141.71.28:83","60.214.100.134:10001")
    #print(nurl)
    mysql = pymysql.connect(host='127.0.0.1',user='root', password='123456', port='3306', db='Xztest')
    cursor = mysql.cursor()
    while True:  
        # start_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:00', '%Y-%m-%d%H:%M')
        # end_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '9:30', '%Y-%m-%d%H:%M')
        # now_time = datetime.datetime.now()
        # if start_time<now_time<end_time:
        try:
            consiquent_fail = 0  # 连续失败帧数
            max_consiquent_fail = 50  # 最大连续失败帧数

            while True:
                cap = cv2.VideoCapture(nurl)
                ret, frame = cap.read()
                # 取流失败
                if not ret:
                    consiquent_fail += 1
                    if consiquent_fail >= max_consiquent_fail:
                        break  # 失败过量则重连 cap
                # 取流成功
                else:
                    for j in range(3):
                        cur_time = int(round(time.time()*1000))
                        standart_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                        save_path = path_unhanded + cur_time + ".jpg"
                        cv2.imwrite(save_path , frame[:,:,::-1])
                        res = detect.run(weights='weights/best.pt', source = save_path, project='ai-dispose' ,name = '100121')
                        # if len(res):
                        #     sql = 'insert into t_ai_img values (%s,%s,%s,%s)'
                        #     param = ('ai-dipose/100121/'+cur_time+'.jpg','煤堆未覆盖',standart_time,cur_time)
                        #     cursor.execute(sql,param)
                        #     mysql.commit()
                        for img in res:
                            cur_time = int(round(time.time()*1000))
                            standart_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                            size = os.path.getsize('ai-dispose/100121/'+img)/1024
                            sql = 'insert into t_ai_img(video_no, label, img_url, create_time, video_url, img_no, size, update_time) values (%s,%s,%s,%s,%s,%s,%s,%s)'
                            param = ('37046803001310516439','裸漏煤堆/物料堆场扬尘识别','1111',standart_time,'2222',cur_time,size,standart_time)
                            cursor.execute(sql,param)
                            mysql.commit()
                        i = i + 1
                        time.sleep(60)
                    time.sleep(1800)
                    break

        except cv2.error as err:
            print(err)
            continue
    mysql.close()
    cursor.close()
mysql = pymysql.connect(host='127.0.0.1',user='root', password='123456', port=3306, db='Xztest')
cursor = mysql.cursor()


res = detect.run(weights='weights/best.pt', source = 'unhanded', project='ai-dispose' ,name = '100121')
print(res)
# if len(res):
#     sql = 'insert into t_ai_img values (%s,%s,%s,%s)'
#     param = ('ai-dipose/100121/'+cur_time+'.jpg','煤堆未覆盖',standart_time,cur_time)
#     cursor.execute(sql,param)
#     mysql.commit()
for img in res:
    cur_time = int(round(time.time()*1000))
    standart_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    size = os.path.getsize('ai-dispose/100121/'+img)/1024
    sql = 'insert into t_ai_img(video_no, label, img_url, create_time, video_url, img_no, size, update_time) values (%s,%s,%s,%s,%s,%s,%s,%s)'

    param = ('37046803001310516439','裸漏煤堆/物料堆场扬尘识别','1111',standart_time,'2222',cur_time,size,standart_time)
    cursor.execute(sql,param)
    mysql.commit()
mysql.close()
cursor.close()