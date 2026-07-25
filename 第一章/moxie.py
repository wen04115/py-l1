def add(a,b):
   return a+b
print(add(3,5))

def check_age(age):
    if age>=18:
        return("成年")
    else:
         return("未成年") 
print(check_age(20))          
print(check_age(15))

def greet(name):
   return(f"你好，{name}！")
print(greet("小明"))