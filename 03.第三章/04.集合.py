# 根据提供的班级学生的选课情况，完成如下需求：
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子", "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = {"遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
# 1找出同时选修了法语和艺术的学生
# 法1：fayi=french_set.intersection(art_set)
# print("同时选修了法语和艺术的学生有:",fayi)
# 法2:fayi=french_set & art_set
# print("同时选修了法语和艺术的学生有:",fayi)

# 2找出同时选修了所有四门课程的学生
# simen=football_set & basketball_set& french_set & art_set
# print("同时选修了所有四门课程的学生有:",simen)

# 3找出选修了足球，但是没有选修篮球的学生
# 法1：chaji=football_set.difference(basketball_set)
# 法2:cha=football_set-basketball_set
# print("找出选修了足球，但是没有选修篮球的学生有:",chaji,cha)
# fb_set={s for s in football_set if s not in basketball_set}
# print("找出选修了足球，但是没有选修篮球的学生有:",fb_set)
# 4统计每一个学生选修的课程数量
# 1.先获取所有学生名单
# 法一：all_set={football_set.union(basketball_set).union(french_set).union(art_set)} 集合不能存储相同元素
# 法二:all_list=[football_set | basketball_set | french_set | art_set]
all_set=football_set.union(basketball_set).union(french_set).union(art_set)
# 获取某个学生选修的课程数量
all_list=[*football_set,*basketball_set,*art_set,*french_set] #解包,把集合解开放在列表中
for i in all_set:
   print(f"{i}的选修课程数量为{all_list.count(i)}")


