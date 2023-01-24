import requests

# 盲注主函数
def StartSqli(url):
    GetDBName(url)
    print("[+]当前数据库名:{0}".format(DBName))


# 获取数据库名函数
def GetDBName(url):
    # 引用全局变量DBName,用来存放网页当前使用的数据库名
    global DBName
    print("[-]开始获取数据库名长度")
    # 保存数据库名长度变量
    DBNameLen = 0
    for DBNameLen in range(1,100):
        



# main 函数
if __name__ == '__main__':
    url = 'http://e2df23b3-84f5-44e4-9eba-3134fe22b56e.node4.buuoj.cn:81/index.php'
    StartSqli(url)