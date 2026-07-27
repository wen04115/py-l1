# 将用户输入的 10 个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值和平均值。
# num_list=[]
# for i in range(10):
#     num=int(input("请输入数字:"))
#     num_list.append(num) 
# num_list.sort()
# print(f"排序后的列表为:{num_list}")
# print(f"最小值为:{num_list[0]}")
# print(f"最大值为:{num_list[9]}")
# print(f"平均值为{sum(num_list)/len(num_list)}")

# 合并两个列表中的元素，并对合并的结果进行去重处理（去除列表中的重复元素）
# python
# 运行
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# num_list=[]
# new_list=[]
# # 合并列表
# num_list=num_list1+num_list2
# print("合并后的列表为:",num_list)
# for num in  num_list:
#     if num not in new_list:
#         new_list.append(num)  
# print(new_list)        

# 生成 1–20 的平方列表。
# num_list=[]
# for num in range(1,21):
#     num_list.append(num**2)
# print(num_list) 
# 方法二
# num_list=[num**2 for num in range(1,21)]
# print(num_list)   
# 给定列表 ，提取所有偶数，计算偶数平方，组成新列表
# num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
# num_list1=[i**2 for i in num_list if i%2==0]
# print(num_list1)

# 将三个列表合并为一个列表，去重、升序排序后输出
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
# list=list1+list2+list3
# num_list=[]
# for num in list:
#     if num not in num_list:
#         num_list.append(num)
# print("合并后的列表为:",list)        
# print("去重后的列表为:",num_list)
# num_list.sort()
# print("升序排序后的列表为:",num_list)  
      
# 提取列表中能被 3或5 整除的数字，求平方组成新列表
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# list=[i**2 for i in list1 if i%3==0 or i%5==0 ]
# print(list)
# 提取列表里面所有正数，组成新列表
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
list=[i for i in list1 if i>0]
print(list)