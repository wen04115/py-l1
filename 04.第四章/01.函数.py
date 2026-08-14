# 函数定义
# def out_line():  #先定义
#     print("-----------")
#     print("-----------")

# out_line()  #调用  

# 函数的参数与返回值
# # 1.计算圆的面积
# def circle_area(r):
#     area=3.14**2*r
#     return area
# area=circle_area(10)    
# print("圆的面积是:",area)    

# 2.计算长方形的面积
# def rectangle_area(l,w):
#     area=l*w
#     return area
# print("长方形的面积是:",rectangle_area(2,3))
# 
# 3.多个返回值  计算圆的面积,周长
# def circle_area_len(r):
#     """
#        根据半径求出圆的面积周长

#     """
#     return r**2*3.14,round(2*3.14*r,1)
# # al=circle_area_len(10)
# area,len=circle_area_len(10)      #解包
# #help(circle_area_len)
# print(area)
# print(len)    


# 函数嵌套调用
#案例一
#定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）
# def triangle_area(d,h):
#     return (d*h)/2
# d=int(input("请输入三角形的底:")) 
# h=int(input("请输入三角形的高:"))   
# print("三角形面积为:",triangle_area(d,h))

#案例二
# 定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）
# def vowel_count(s):
#     count=0
#     for i in s:
#         if i in "aeiouAEIOU":
#             count+=1
#     return count
# s=input("请输入字符串:")
# vowel_count(s)    
# print("传入的字符串中元音字母的个数为:",vowel_count(s))            
#案例三  
#定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分 (保留 1 位小数)，并返回 不知道总人数
# def gaokao_score(score_list):
#     return max(score_list),min(score_list),round(sum(score_list)/len(score_list),1)
# score_list=[]
# while True:
#     s=int(input("请输入分数:"))
#     if s== -1:
#         break
#     else:
#        score_list.append(s) 
# gaokao_score(score_list)
# max_score,min_score,avg_score=gaokao_score(score_list)
# print(f"列表中成绩的最高分:{max_score} 最低分:{min_score} 平均分{avg_score}")   
# 
#函数传参方式
# 定义函数
# def reg_stu(name, age, gender, city):
#     print(f"注册成功，姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#     return {"name": name, "age": age, "gender": gender, "city": city} 
# # 传参方式一：位置参数
# # stu=reg_stu("张三",18,"男","北京")
# # print(stu)

# # 传参方式二:关键字参数(参数传递顺序可以不一致)
# stu=reg_stu(age=18,name="张三",gender="男",city="北京")

# # 传参方式三:位置参数+关键字参数  必须位置参数在前,位置参数有顺序要求，关键字参数在后面
# stu=reg_stu("张三",18,gender="男",city="北京")
    
# 默认值
# def reg_stu(name, age, gender="男", city="北京"):
#      print(f"注册成功，姓名: {name}, 年龄: {age}, 性别: {gender}, 城市: {city}")
#      return {"name": name, "age": age, "gender": gender, "city": city}    
#  stu=reg_stu("张三",18)
# print(stu)

# stu=reg_stu("张三",18,"女","北京") 
# print(stu) 
 
# stu=reg_stu("张三",18,city="上海") 
# print(stu) 

# 不定长参数
# 根据传入的这批数据,计算这批数据的最大最小平均值 位置传递
# def cal_data(*args):
#     min_data=min(args)
#     max_data=max(args)
#     avg_data=sum(args)/len(args)
#     return min_data,max_data,round(avg_data,1)
# print(cal_data(2,7,9,10,45,73,37,93,92,111,222)) 


# 关键字传递
# def calc_data(*args, **kwargs):
#     """
#     根据传入的这批数据，计算这批数据的最小值，最大值，平均值
#     :param args: 不定长位置参数，需要计算的这批数据
#     :param kwargs: 不定长关键字参数
#         round: 保留的小数位个数
#         print: 是否打印输出
#     :return: 最小值，最大值，平均值
#     """
#     min_data = min(args)
#     max_data = max(args)
#     avg_data = sum(args) / len(args)

#     # =========使用kwargs里的round=========
#     if "round" in kwargs:
#         avg_data = round(avg_data, kwargs["round"])

#     # =========使用kwargs里的print=========
#     if kwargs.get("print"):
#         print(f"最小值:{min_data},最大值:{max_data},平均值:{avg_data}")

#     return min_data, max_data, avg_data


# # 调用
# res = calc_data(2, 7, 9, 10, 45, round=3, print=True) #小数位数超过3位就保持三位小数,没超过三位就按本身来
# print("函数返回结果：", res)

# 匿名函数
# 需求1:打印一个分割线
# 本来逻辑:
# def out_line():
#    print("-----") 
# 匿名逻辑:out_line=lambda : print("-----")
# out_line()

# 需求2:计算两个数的和
# 本来逻辑:
# def add(x,y):
#    return(x+y)
# 匿名逻辑
# add=lambda x,y:x+y
# print(add(10,20))

# 需求3：完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；
# data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
# data_list.sort(key=lambda item :len(item))
# print(data_list)