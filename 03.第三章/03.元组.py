# 现有三个变量，分别为a=100,b=200,c=300 现需要将这三个变量值进行交换，将a,b,c的值分别赋值给c,b,a，并将其输出到控制台
# a,b,c=100,200,300
# a,b,c=c,b,a  #元组的组包与解包
# print(a,b,c)

# 根据提供的学生成绩单，完成如下需求：
# 计算每个学生的总分、各科平均分，然后一并输出出来。
# 统计各科成绩的最低分、最高分、平均分，并输出。
# 查找成绩优秀（平均分大于 90）的学生，并输出。
# 装一堆同学的成绩且不用增删改 所以用元组
# s=(
#     ("S001","王林",85,92,78),
#     ("S002","李慕婉",92,88,95),
#     ("S003","十三",78,85,82),
#     ("S004", "曾牛", 88,79,91),
#     ("S005", "周轶", 95,96,89),
#     ("S006", "王卓", 76, 82, 77),
#     ("S007", "红蝶", 89, 91, 94),
#     ("S008", "徐立国", 75, 69, 82),
#     ("S009", "许木", 86, 89, 98),
#     ("S010", "遁天", 66, 59, 72)
# )
# print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
# for num in s:
#     total=num[2]+num[3]+num[4]
#     avg=total/3.0
#     print(f"{num[0]}\t{num[1]}\t{num[2]}\t{num[3]}\t{num[4]}\t{total}\t{avg:.1f}")
# chinese=[]
# math=[]    
# english=[]
# for num in s:
#     chinese.append(num[2])
#     math.append(num[3])
#     english.append(num[4])
# print(f"语文最低分是{min(chinese)},数学最低分是{min(math)},英语最低分是{min(english)}")    
# print(f"语文最高分是{max(chinese)},数学最高分是{max(math)},英语最高分是{max(english)}")
# print(f"语文平均分是:{sum(chinese)/len(chinese):.1f},数学平均分是:{sum(math)/len(math):.1f},英语平均分是:{sum(english)/len(english):.1f}")
# print("优秀学生名单如下")
# for num in s:
#     avg= (num[2]+num[3]+num[4])/3.0
#     if avg>90:
#         print(f"{num[0]}\t{num[1]}\t平均分{avg:.1f}")

# 优化
s=(
    ("S001","王林",85,92,78),
    ("S002","李慕婉",92,88,95),
    ("S003","十三",78,85,82),
    ("S004", "曾牛", 88,79,91),
    ("S005", "周轶", 95,96,89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)
print("学号\t姓名\t语文\t数学\t英语\t总分\t平均分")
# 元组解包
for id,name,chinese,math,english in s:
    total=chinese+math+english
    avg=total/3.0
    print(f"{id}\t{name}\t{chinese}\t{math}\t{english}\t{total}\t{avg:.1f}")
chinese=[]
math=[]    
english=[]
for num in s:
    chinese.append(num[2])
    math.append(num[3])
    english.append(num[4])
print(f"语文最低分是{min(chinese)},数学最低分是{min(math)},英语最低分是{min(english)}")    
print(f"语文最高分是{max(chinese)},数学最高分是{max(math)},英语最高分是{max(english)}")
print(f"语文平均分是:{sum(chinese)/len(chinese):.1f},数学平均分是:{sum(math)/len(math):.1f},英语平均分是:{sum(english)/len(english):.1f}")
print("优秀学生名单如下")
for id,name,chinese,math,english in s:
    avg= (chinese+math+english)/3.0
    if avg>90:
        print(f"学号:{id}\t姓名: {name}\t平均分: {avg:.1f}")