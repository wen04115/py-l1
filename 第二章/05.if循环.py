# if条件判断
# score=700
# if score>680:
#     print("恭喜你考上重点大学")
# print("------")   


# 需求：结合前面学习的输入输出及 if 条件判断的知识，完成 B 站登录功能的实现（正确账号和密码为 18888888888/6668888）。
# zhanghu=input("请输入账号:")
# keyboard=input("请输入密码:")
# if zhanghu=="18888888888"and keyboard=="6668888":
#     print("登录成功")
# else:
#     print("登录失败")


# 根据用户输入的年份，判断这一年是闰年还是平年。
# 非整百年份，且能被 4 整除的年份是闰年
# 整百年份（如 1900 年、2000 年）必须能被 400 整除才是闰年
# year=int(input("请输入年份:"))
# if year%4==0  and  year%100!=0:
#     print("是闰年")
# elif  year%100==0 and year%400==0:
#     print("是闰年")
# else:
#     print("是平年")

# 需求 1：根据用户输入的数字，判断该数字是奇数还是偶数。
# num=int(input("请输入一个数字:"))
# if num%2==0:
#     print("偶数")
# else:
#     print("奇数")

# 需求 2：根据用户输入的年龄，判断该用户是否已经成年（>=18，成年；否则，未成年）。
# year=int(input("请输入年龄:"))
# if year>=18:
#     print("成年")
# else:
#     print("未成年")

# 需求 3：根据用户输入的数字，判断该数字是正数还是负数（不考虑 0）。
# num=float(input("请输入一个数字:"))
# if num<0:
#     print("负数")
# else:
#     print("正数")

# 需求 4：根据用户输入的考试分数，判断该分数是否及格了（大于等于 60 就是及格了）。 
# score=float(input("请输入考试分数:"))
# if score>=60:
#     print("及格")
# else:
#     print("不及格")

# 根据用户输入的数字，判断该数字是正数还是负数还是0
# num=float(input("请输入一个数字:"))
# if num>0:
#     print("正数")
# elif  num<0:
#     print("负数")
# else:
#     print("该数是0")


# 根据输入用户名、密码进行登录系统。
# 用户名、密码为 admin/6668888 或 root/547527 或 zhangsan/123456，则输出登录成功
# 否则就提示用户名或密码错误

# zhanghao=input("请输入用户名:")
# password=input("请输入密码:")
# if zhanghao=="admin" and password=="6668888":
#     print("登录成功")
# elif zhanghao=="root"and password=="547527":
#     print("登录成功")
# elif zhanghao=="zhangsan"and password=="123456":
#     print("登录成功")
# else:
#     print("用户名或密码错误")    

# 需求 1：成绩等级判断
# 根据输入的考试成绩，判断成绩等级。
# 大于等于 85 分为优秀
# 60-85 分为及格
# 否则就是不及格
# score=float(input("请输入考试成绩:"))
# if score>=85:
#     print("优秀")
# elif  score>=60 and score<=85:
#     print("及格")
# else:
#     print("不及格")

# 需求 2：购物折扣计算
# 购物折扣计算：根据输入的购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。
# 金额 >= 500：8 折
# 300 <= 金额 < 500：9 折
# 100 <= 金额 < 300：95 折
# 金额 < 100：无折扣
# money=float(input("请输入购物车的商品总额:"))
# if money>=500:
#     print("8折,实付金额为:",money*0.8)
# elif money>=300 and money<500:
#     print("9折,实付金额为:",money*0.9)
# elif money>=100 and money<300:
#     print("95折,实付金额为:",money*0.95)
# else:
#     print("无折扣,支付金额为:",money)

# 需求：三角形类型判断
# 根据输入的三个边的边长 (正整数)，判定是等边三角形、等腰三角形、普通三角形，还是不能构成三角形。
# 构成三角形的条件：任意两边之和大于第三边
# 三角形判定规则：
# 三个边都相等：等边三角形
# 两个边相等：等腰三角形
# 三个边都不相等：普通三角形
# a=float(input("请输入第一个边的边长:"))
# b=float(input("请输入第二个边的边长:"))
# c=float(input("请输入第三个边的边长:"))
# if (a+b>c and b+c>a and a+c>b) and a==b==c:
#     print("等边三角形")
# elif (a+b>c and b+c>a and a+c>b) and (a==b or b==c or a==c):
#     print("等腰三角形")
# elif (a+b>c and b+c>a and a+c>b) and (a!=b!=c):
#     print("普通三角形")
# else:
#       print("不是三角形")      

# 北京市居民年度用电电费计算：根据输入的用电度数，计算电费
# 北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
# 阶梯电价规则：
# 第一档：2880 度以下，电费单价 0.4883 元 / 度
# 第二档：2880-4800 度，电费单价 0.5383 元 / 度
# 第三档：4800 度以上，电费单价 0.7883 元 / 度
# num=float(input("请输入用电数"))
# if num<2880:
#     money=num*0.4883
# elif num>=2880 and num<=4800:
#     money=0.4883*2880+(num-2880)*0.5383
# else:
#     money=2880*0.4883+1920*0.5383+(num-4800)*0.7883
# print("电费是：",money)        

        