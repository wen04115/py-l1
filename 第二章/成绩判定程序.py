# 成绩判定程序
score=float(input("请输入分数:"))
match score:
    case __ if score>=90 and score<=100: print("该成绩为A优秀")
    case _ if score>=80 and score<=89: print("该成绩为B 良好")
    case _ if  score>=70 and score<=79: print("该成绩为C 中等")
    case _ if  score>=60 and score<=69: print("该成绩为D 及格")
    case _ if  score>=0 and score<=59: print("该成绩为不及格")
    case _:print("输入不符合要求")


