# print("10+4=",10+4)
# print("10/4=",10/4)
# print("10//4=",10//4)
# print("10**4=",10**4)

# 算数优先级运算符** ，*， / // %， + -

# 输入两个数x,y 求x+y x-y的结果
# x=input("请输入第一个数:")
# y=input("请输入第二个数:")
# h=int(x)+int(y)
# c=int(x)-int(y)
# print(h)
# print(c)

# 计算输入的三个整数的平均数
# a=int(input("请输入第一个数:"))
# b=int(input("请输入第二个数:"))
# c=int(input("请输入第三个数:"))
# ave=(a+b+c)//3
# print(ave)

# 输入梯形的上底 下底 高 计算梯形的面积
# shang=float(input("请输入上底:"))
# xia=float(input("请输入下底:"))
# high=float(input("请输入高:"))
# s=(shang+xia)*high/2
# print(s)

# 输入圆的半径 计算圆的周长和面积
# ban=float(input("请输入圆的半径:"))
# chang=2*3.14*ban
# mianji=3.14**2*ban
# print(f"圆的周长:{chang}")
# print(f"圆的面积:{mianji}")

# 身体质量指数BMI计算（BMI=体重kg/身高m2）
# tizhong=float(input("请输入体重:"))
# shengao=float(input("请输入身高:"))
# BMI=tizhong/(shengao*shengao)
# print("BMI是:%s"  %BMI)

# num=85
# num/=10
# print(num) #print(num/=10)
# print(num/=10) 错误 赋值运算符没有返回值，不允许作为print的参数

# 逻辑运算符
# 键盘输入一个数判断这个数是否在10-20之间
# a=input("请输入一个数:")
# n=int(a)
# print(f"{n}在10-20之间：",n>=10 and n<=20)

# 键盘输入一个数判断这个数是否不在10-20之间
a=input("请输入一个数:")
n=int(a)
print(f"{n}不在10-20之间：",n<10 or n>20)