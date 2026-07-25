# 计算1-100之间所有奇数之和
# sum=0
# for i in range(1,101):
#     if i%2!=0:
#         sum+=i
#     i+=1
# print(f"1-100之间所有奇数之和:{sum}")   
# 简化
sum=0
for i  in range(1,101,2):
    sum+=i
print(f"1-100之间所有奇数之和:{sum}")     
# 计算100-500之间所有3的倍数的数字之和
# sum=0
# for i in range(100,501):
#     if i%3==0:
#       sum+=i
#     i+=1    
# print(f"300-500之间所有3的倍数的数字之和:{sum}")    