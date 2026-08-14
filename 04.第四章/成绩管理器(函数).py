menu="""
   ===== 学生成绩管理器 =====
1. 录入成绩
2. 计算总分
3. 计算平均分
4. 查找最高/最低分
5. 判断等级
6. 退出
==========================
"""
def calc_total(scores):
    return sum(scores)

def calc_average(scores):
    if not scores:
        return 0
    return round(sum(scores) / len(scores), 1)

def find_max_min(scores):
    return max(scores), min(scores)

def get_grade(score):
    if score >= 90:
        return "优秀"
    elif score >= 80:
        return "良好"
    elif score >= 60:
        return "及格"
    else:
        return "不及格"
def show_all(names, scores, title="成绩单"):
    print(f"===== {title} =====")
    for name, score in zip(names, scores):
        grade = get_grade(score)    # ← 调用上面写好的函数
        print(f"{name}: {score} ({grade})")        

def score_manage(*args):     
 while True:
   num=input("请输入数字:")
   match num:
    case "1":
      name=input("请输入姓名:")
      score=float(input("请输入成绩:"))
      name_list.append(name)
      score_list.append(score)
      print("录入完成！") 
    case "2":
        total = calc_total(score_list)   # 调用函数
        print(f"总分: {total}")
    case "3":
        avg = calc_average(score_list)
        print(f"平均分: {avg}")
    case "4":
        if not score_list:
         print("暂无数据！")
        else:
         max_s, min_s=find_max_min(score_list)
         print(f"最高分: {max_s}, 最低分: {min_s}")
    case "5":
        show_all(name_list,score_list)
            
    case "6":
        print("退出")
        break
    case _:
        print("输入数字错误,请重新输入")
                             
name_list=[]
score_list=[]
score_manage()

print(score_manage)
#print(score_manage(name_list,score_list))
# ("小明",60),("小蓝",80),("小红",70),("小王",50),("小赵",90)