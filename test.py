import requests
import time

url = 'http://www.hnsydwpx.cn/learning/coursenoderecord/heartbeat'
# 注意这里必须以json字符串构造数据
chapterId = 0
courseId = 0
nodeId = 0

learningToken = ""
learningTime = 120

#个人参数
studentId = "1080197"
cookie1 = "JSESSIONID=g8FDqSbKsjTV6Llj3FjyICLk7v_aZOYXFfvu4oFN"
classesId = "563458097020928000"


headers = {
'POST /learning/coursenoderecord/heartbeat HTTP/1.1'
'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Authorization': 'Bearer 74c85184-a279-486a-b010-15b9e7a2a8ce',
'Connection': 'keep-alive',
'Content-Length': '196',
'Content-Type': 'application/json',
'Cookie': cookie1,
'Host': 'www.hnsydwpx.cn',
'Origin': 'http://www.hnsydwpx.cn',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'
}

#课程集合
array = [#['10908','10845','13554'],#0
#['10908','10845','13555'],#1
#['10908','10845','13556'],#2
#['10909','10846','13558'],#3
#['10909','10846','13559'],#4
#['10910','10847','13560'],#5
#['10910','10847','13561'],#6
#['10910','10847','13562'],#7
#['10911','10848','13563'],#8
#['10911','10848','13564'],#9
#['10911','10848','13565'],#10
#['10912','10849','13566'],#11
#['10912','10849','13567'],#12
#['10912','10849','13568'],#13
#['10913','10850','13569'],#14
#['10913','10850','13570'],#15
#['10913','10850','13571'],#16
#['10914','10851','13572'],#17
#['10914','10851','13573'],#18
#['10915','10852','13574'],#19
['10915','10852','13575'],#20
['10915','10852','13576'],#21
['10916','10853','13577'],#22
['10916','10853','13578'],#23
['10916','10853','13579'],#24
['10916','10853','13580'],#25
['10917','10854','13581'],#26
['10918','10855','13582'],#27
['10918','10855','13583'],#28
['10918','10855','13584'],#29
['10918','10855','13585'],#30
]

i = 0
while i < len(array):
    chapterId = array[i][0]
    courseId = array[i][1]
    nodeId = array[i][2]
    i += 1
    #获取Token
    payloadGetToken = {"chapterId":chapterId,"classesId":classesId,"courseId":courseId,"learningToken":"","nodeId":nodeId,"sourceType":1,"studentId":1080197,"viewingLength":0}
    r = requests.post(url, json=payloadGetToken , headers=headers)
    learningToken = r.json()["data"]['data']
    time.sleep(2)

    #赋值
    payloadLearning = {"chapterId":chapterId,"classesId":classesId,"courseId":courseId,"learningToken":learningToken,"nodeId":nodeId,"sourceType":1,"studentId":1080197,"viewingLength":learningTime}

    #开始学习
    x = 0
    while x < 30:
        print("开始学习")
        time.sleep(learningTime)
        r2 = requests.post(url, json=payloadLearning , headers=headers)
        # 查看响应结果
        print(r.json())
        print(r2.json())
        x += 1








