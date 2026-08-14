#__all__ 是一个模块级别的特殊变量，用于指定 from 模块名 import * 时会导入哪些功能（* 通配匹配哪些功能)
__all__ = ["log_separator1","log_separator3","PI"]  #连续按两下0旁边的-

# 常量(不会发生变化的数据；常量的名称为全部大写)
PI = 3.1415926
NAME = "黑马☆涛哥"

# 函数
def log_separator1():
    print("- " * 30) # "- " 重复输出30次

def log_separator2():
    print("+ " * 30)

def log_separator3():
    print("# " * 30)

def log_separator4():
    print("* " * 30)

# 测试函数
if __name__ == "__main__":  #不管文件名叫什么 测试的时候都写这个
 log_separator1()