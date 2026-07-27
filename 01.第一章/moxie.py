#1.def add(a,b):
#    return a+b
# print(add(3,5))

# 2.def check_age(age):
#     if age>=18:
#         return("成年")
#     else:
#          return("未成年") 
# print(check_age(20))          
# print(check_age(15))

# 3.def greet(name):
#    return(f"你好，{name}！")
# print(greet("小明"))

# 4.score=float(input("请输入分数："))
# if score>=90:
#    print("优秀")
# elif score>=60 and score<90:
#    print("及格")
# else:
#    print("不及格")

# 5.score=float(input("请输入分数："))
# match score:
#    case _ if score>=90: print("该分数为A优秀")
#    case _ if score>=80 and score<90: print("该分数为B良好")
#    case _ if score>=60 and score<80: print("该分数为C及格")
#    case _ if score<60: print("该分数不及格")

# 6.猜数字
# import random
# num=random.randint(1,100)
# num1=int(input("请输入数字"))
# count=0
# while True:
#    if num1>num:
#       print("猜大了")
#       count+=1
#       num1=int(input("请重新输入数字"))
#    elif num1<num:
#       print("猜小了")
#       count+=1
#       num1=int(input("请重新输入数字"))
#    else:
#       count+=1
#       print(f"猜对了,共猜了{count}次")
#       break      

# 7.for i in range(1,10):
#    print(i)

# 8.name=input("请输入姓名:")
# age=input("请输入年龄:")
# print(f"我是{name},今年{age}岁")


