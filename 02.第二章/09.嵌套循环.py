# 循环嵌套：根据输入的长方形的长度 m，宽度 n ，打印一个长方形；
# 如下：是一个长度为 10，宽度为 5 的长方形
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# m=int(input("请输入长方形的宽度：")) #控制行
# n=int(input("请输入长方形的长度：")) #控制列
# for j in range(m):
#     for i in range (n):
#         print("*",end=" ")
#     print()    

# 打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}x{i}={i*j}",end="\t")
#     print()    

# 根据输入的直角边的边长，打印等腰直角三角形（示例：直角边为 5）
# *
# * *
# * * *
# * * * *
# * * * * *
# i=int(input("请输入边长:"))
# for i in range(1,i+1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()    
# 根据输入的数字，打印对应的数字金字塔
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# i=int(input("请输入数字:"))
# for i in range(1,i+1):
#     for j in range(1,i+1):
#         print(j,end="   ")
#     print()    
# 打印国际象棋棋盘
# ■ □ ■ □ ■ □ ■ □
# □ ■ □ ■ □ ■ □ ■
# ■ □ ■ □ ■ □ ■ □
# □ ■ □ ■ □ ■ □ ■
# ■ □ ■ □ ■ □ ■ □
# □ ■ □ ■ □ ■ □ ■
# ■ □ ■ □ ■ □ ■ □
# □ ■ □ ■ □ ■ □ ■
# for i in range(8): #行数
#     for j in range(4): #列数
#         if i%2==0:
#          print("■  □",end="  ")
#         else:
#          print("□  ■",end="  ")    
#     print()   
# 
# 需求：根据输入的用户名密码执行登录操作，具体要求如下：
# 正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666
# 输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
# 输入的用户名和密码不能为空！
# 登录成功：输出 "登录成功，进入B站首页~"
# 登录失败：输出 "用户名或密码错误，请重新输入！" 
# yonghu=input("请输入用户名:")
# password=input("请输入密码:")
# while True:
#     if (yonghu=="admin" and password=="666888")or(yonghu=="zhangsan" and password=="123456")or(yonghu=="taoge" and password=="888666"):
#         print("登录成功,进入B站首页~")
#         break
#     elif yonghu==""or password=="":
#         print("用户名和密码不能为空！")
#         yonghu=input("请重新输入用户名:")
#         password=input("请重新输入密码:")
#     else:
#         print("用户名或密码错误，请重新输入！")
#         yonghu=input("请重新输入用户名:")
#         password=input("请重新输入密码:")    
# 
# 需求：用户名密码登录，正确的用户名和密码为admin/666888、zhangsan/123456、taoge/888666，
#5 次登录机会，输入错误五次，不允许再操作了。
# num=1
# while True:
#     yonghu=input("请输入用户名:")
#     password=input("请输入密码:")
#     if num<=4:
#        if (yonghu=="admin" and password=="666888"):
#          print("登录成功,进入B站首页~")
#          break
#        elif  yonghu=="zhangsan" and password=="123456":
#           print("登录成功,进入B站首页~")
#           break
#        elif yonghu=="taoge" and password=="888666":
#           print("登录成功,进入B站首页~")
#           break
#        else:
#          print("用户名或密码错误，请重新输入！")
#          num+=1
#          continue
#     else:
#        print("次数超过五次，不允许操作")
#        break         

# 猜数字游戏
# 系统随机生成一个随机数
# 用户根据提示猜数字，并将所猜的数字输入系统
# 如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
# 如果猜对，系统自动退出，游戏结束
# import random
# num=random.randint(1,100)      
# while True:
#      num1=int(input("请输入数字:"))
#      if num1<num:
#         print("猜小了")
#      elif num1>num:
#          print("猜大了")
#      else:
#         print("猜对了，游戏结束")
#         break   
   
# 将 1-1000 之间（含 1000）所有的 5 的倍数的数字累加起来
# sum=0
# for i in range(1,1001):
#     if i%5==0:
#         sum+=i
# print(f"累加结果为:{sum}")        
# 统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 中有多少个a和k
string="akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
sum,num=0,0
for i in string:
    if i=="a":
        sum+=1
    elif i=="k":
        num+=1
print(f"共有{sum}个a和{num}个k")           