import main  #导入自己定义的模块，模块名就是文件名 不用加.py

print(main.PI)  #没导入功能名，所以要加上模块名
main.log_separator3()
# from main import log_separator2  #导入谁才能调用谁，没导入不能调用，比如没导入log_separator3 所有不能使用这个函数
# log_separator2()

from main import *  #导入所有功能 但是all里没有2，所有报错
print(PI)
log_separator3()