# 计算1-100之间所有偶数的和
i=1
sum=0
while i>=1 and i<=100:
    if i%2==0:
        sum+=i
    i+=1
print(f"1-100之间所有偶数之和为:{sum}")        