# 需求：实现一个计算器，可以实现 + - * / 运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算。
# x=int(input("请输入第一个数"))
# y=int(input("请输入第二个数"))
# z=input("请输入运算符")
# match z:
#     # case "+" : print("两数相加为：",x+y)
#     # case "-" : print("两数相减为：",x-y)
#     # case "*" : print("两数相乘为：",x*y)
#     # case "/" : print("两数相除为：",x/y)
#     # case _ : print("符号不符合要求")
#     case "+" : print(f"{x}和{y}相加为：{x+y}")
#     case "-" : print(f"{x}和{y}相减为：{x-y}")
#     case "*" : print(f"{x}和{y}相乘为：{x*y}")
#     case "/" : print(f"{x}和{y}相除为：{x/y}")
#     case _ : print("符号不符合要求")

# 编写一个游戏角色移动控制系统，根据玩家输入的不同指令，控制游戏角色执行相应动作。
# 玩家输入	对应动作
# 上 /w/ W	角色向上移动
# 下 /s/ S	角色向下移动
# 左 /a/ A	角色向左移动
# 右 /d/ D	角色向右移动
# 跳 / 空格	角色跳跃
# 攻击 /j/ J	角色发动攻击
# 退出 /esc/ ESC	角色退出游戏
# zhiling=input("请输入指令")
# match zhiling:
#     case "上"|"w"|"W": print(f"输入{zhiling},角色向上移动")
#     case "下"|"s"|"S": print(f"输入{zhiling},角色向下移动")
#     case "左"|"a"|"A": print(f"输入{zhiling},角色向左移动")
#     case "右"|"d"|"D": print(f"输入{zhiling},角色向右移动")
#     case "跳"|"空格": print(f"输入{zhiling},角色跳跃")
#     case "攻击"|"j"|"J": print(f"输入{zhiling},角色发动攻击")
#     case "退出"|"esc"|"ESC": print(f"输入{zhiling},角色退出游戏")
#     case _: print("指令不符合要求")

