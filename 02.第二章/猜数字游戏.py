import random
num=int(input("请输入数字"))
num1=random.randint(1,100)
count=0
while True:
    if num>num1:
        print("猜大了")
        num=int(input("请重新输入数字"))
        count+=1
    elif  num<num1:
          print("猜小了")
          num=int(input("请重新输入数字"))
          count+=1
    else:
        count+=1
        print(f"猜对了,一共猜了{count}次")
        break         