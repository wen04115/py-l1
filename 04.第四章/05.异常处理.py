# try:
#     print("--------------")
#     print(my_name)
#     print("--------------")
# except NameError as e :
#     print("程序出错，联系管理员",e) 
# 
# 
try:
    print("--------------")
    #print(my_name)
    #print(1/0)
    print("ABC"[10])
    print("--------------")
except NameError as e :
    print("名字不存在，请检查异常信息",e)

except ZeroDivisionError as e :
    print("0不能做除数,请检查异常信息",e)

except IndexError as e :
    print("索引出错，请检查异常信息",e)

except  Exception as e:  #捕获所有异常
    print("程序运行出错，请联系管理员")

finally:    #无论程序是否正常运行，finally里的代码都会运行
   print("资源释放")  
