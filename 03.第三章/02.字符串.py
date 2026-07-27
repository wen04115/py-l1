# 接收用户输入邮箱，满足两个条件：
# 字符串包含且只有 1 个 @
# 字符串至少存在一个 .
# 满足则输出邮箱格式正确，否则邮箱格式错误
# mail=input("请输入邮箱:")
# if mail.count('@')==1 and mail.count('.')>=1:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")

# mail=input("请输入邮箱:")
# if mail.count('@')==1 and '.' in mail:
#      print("邮箱格式正确")
# else:
#      print("邮箱格式错误") 
# 
# 输入字符串，判断是否为回文（正向与反向完全相同，左右对称）
# 示例：黄山落叶松叶落山黄、上海自来水来自海上
# poet=input("请输入字符串:")
# if poet[::-1]==poet:
#     print("是回文")
# else:
#     print("不是回文")
#     print(poet[::-1])
# 用户依次输入 10 个字符串
# 每个字符串先反转，再转为大写
# 存入列表
# 循环遍历列表输出全部内容
num_list=[]
for i in range(3):
    zifu=input("请输入字符串:")
    fanzhuan=zifu[::-1]
    daxie=fanzhuan.upper()
    num_list.append(daxie)
for num in num_list:
    print(num,end=" ")               