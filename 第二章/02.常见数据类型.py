# 查看数据类型 --->
# print("Hello")
# print(type("Hello"))
#
# print(type(10))
# print(type(3.14))
# print(type(True))
# print(type(False))
# print(type(None))
#
# num = -100
# print(type(num))

# 检查数据是否属于指定的类型
# num=100
# print(num)
# print(isinstance(num,float))

# 定义字符串
# 定义字符串的三种方式
# s1="hello"
# s2='python'
# s3="""  1
#       2
#       3
#       """
# print(s1)
# print(s2)
# print(s3)


# 转义字符
# s2='it\'s my good student'
# print(s2)
# print("  欢迎大家学习，\n加油")
# print("\t欢迎大家学习，加油")

# 字符串拼接
# s1="人生苦短 " "我用python" ",ok"
# print(s1)
#
# msg1="人生苦短"
# msg2="我用python"
# print("龟叔说:"+msg1+","+msg2)


# 根据自己的实际情况，输出个人的详细信息，具体结构如下：
# "大家好，我是涛哥，今年 18 岁，学习的专业是软件工程，爱好 Python、Java"
# s1="大家好"
# s2="我是涛哥"
# s3="今年 18 岁"
# s4="学习的专业是软件工程"
# s5="爱好 Python、Java"
# print("\""+s1+","+s2+","+s3+","+s4+","+s5+"\"")

# name="涛哥"
# age=18
# zhuanye="软件工程"
# print("\"大家好，我是"+name+"今年"+str(age)+"岁，学习的专业是"+zhuanye+"爱好 Python、Java\"")

# 占位符
# name="涛哥"
# age=18
# zhuanye="软件工程"
# print("大家好，我是%s，今年 %s岁，学习的专业是%s，爱好 Python、Java" % (name,age,zhuanye))

# 加f
name="涛哥"
age=18
zhuanye="软件工程"
print(f"大家好，我是{name},今年{age}岁，学习的专业是{zhuanye}，爱好 Python、Java")

