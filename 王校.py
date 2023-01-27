# 循环
## for 循环
# for i in range(100):
#     print(i)
# ## while 循环
# times = 100
# while times>0:
#     print("向女神表白")
#     times-=1
# print("女神答应给我了")
# 1+2+...+100
# result = 0
# for i in range(1,101):
#     result = result+i
# print(result)
# for循环的嵌套
# for i in range(10):
#     for j in i:
#         print(j, end=' ')
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end='')
#     print("")
# # 99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{0}x{1}={2}".format(i,j,i*j),end='  ')
#     print("")
#     # f{} %(,,)
# for i in range(9,0,-2):
#     print(i)
# while 99
# i=1
# while i<=9:
#     j = 1
#     while j<=i:
#         print("{0}x{1}={2}".format(i,j,i*j),end='  ')
#         j+=1
#     print("")
#     i+=1
# # for->while 99
# for i in range(1,10):
#     j = 1
#     while j<=i:
#         print("{0}x{1}={2}".format(i,j,i*j),end='  ')
#         j+=1
#     print("")
# # while->for 99
# i=1
# while i<=9:
#     for j in range(1,i+1):
#         print("{0}x{1}={2}".format(i,j,i*j),end='  ')
#     i+=1
#     print("")
# # break continue
# #break->结束循环 continue->结束本循环，进行下一次循环
# for i in range(10):
#     if i==5:
#         # break
#         continue
#     print(i)
# # 拍桌子1-100 print("拍桌子")
# # 递归的99乘法表
# def muti(num):
#     if num<10:
#         for i in range(1,num+1):
#             print("{0}x{1}={2}".format(i,num,i*num),end='  ')
#         print("")
#         muti(num+1)
# muti(1)
for red in range(100):
    for white in range(100):
        for black in range(100):
            if red+white==25 and white+black==31 and red+black==28:
                print('red:',red,'white:',white,'black:',black)
                break