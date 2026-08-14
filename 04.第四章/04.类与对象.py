# #定义类 法一
# class Car:
#     pass

# #基于类创建对象
# c1=Car()

# #动态的为对象添加属性
# c1.color="red"
# c1.brand="BMW"
# c1.name="X5"
# c1.price=500000

# print(c1)
# print(c1.__dict__)  #将对象中的所有属性以字典的形式输出



# 定义类（推荐） 法二
# class Car:
#     #__init__方法是对象初始化的方法，会在对象创建时自动调用，可在该方法中为对象设置对应的属性
#     #self是第一个参数，表示当前所创建的实例对象
#     def __init__(self,c_color,c_brand,c_name,c_price):    
#         self.color=c_color
#         self.brand=c_brand
#         self.name=c_name
#         self.price=c_price
#         print("Car类型的对象初始化完成,对象属性添加完毕")

# #创建对象
# c1=Car("red","BMW","X5",500000)
# print(c1.__dict__)      

# c2=Car("black","BMW","E300l",450000)
# print(c2.__dict__)


#定义类 实例方法
# class Car:
#  def __init__(self,c_color,c_brand,c_name,c_price):    
#         self.color=c_color
#         self.brand=c_brand
#         self.name=c_name
#         self.price=c_price
#         print("Car类型的对象初始化完成,对象属性添加完毕")

# #定义实例方法
 
#  def running(self):
#     print(f"{self.brand},{self.name} 正在高速行驶中")

#  def total_cost(self,discount,rate):   
#     """
#       计算提车的总费用  包含车的价格和税费
#       discount折扣
#       rate税率
#       return 车的总费用
#     """ 
#     total_cost= self.price* discount+ self.price*rate   
#     return  total_cost

# #测试
# c1=Car("red","BMW","X5",500000)  

# #调用对象中的方法
# c1.running()

# total=c1.total_cost(0.9,0.1)
# print("提车的总费用为:",total)


# 魔法方法
# class Car:
#  def __init__(self,c_color,c_brand,c_name,c_price):    
#         self.color=c_color
#         self.brand=c_brand
#         self.name=c_name
#         self.price=c_price
#         print("Car类型的对象初始化完成,对象属性添加完毕")

# #定义实例方法
#  def running(self):
#     print(f"{self.brand},{self.name} 正在高速行驶中")

#  def total_cost(self,discount,rate):   
#     total_cost= self.price* discount+ self.price*rate   
#     return  total_cost
# #魔法方法
#  def __str__(self) :  #str将对象转为字符串
#      return f"{self.color} {self.brand} {self.name} {self.price}"

#  def __eq__(self, other) :  #判断两个对象是否相等
#     return self.color== other.color and self.brand== other.brand and self.name== other.name and self.price== other.price
 
#  def __lt__(self, other):  #判断对象的大小关系
#     return self.price <other.price
# c1=Car("red","BMW","X5",500000)
# print(c1)

# c2=Car("black","BMW","E300l",450000)
# print(c2) 

# print(c1==c2)
# print(c1<c2)


#实例属性与类属性
class Car:
    #类属性(所有实例对象共享)
    wheel=4  #轮胎数量
    tax_rate=0.1  #购置税税率
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel=4

    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中....")

    def total_cost(self, discount, rate=0.1):
        total_cost = self.price * discount + rate * self.price
        return total_cost

# 测试
c1 = Car(c_color="白色", c_brand="BYD", c_name="汉", c_price=180000)
print(c1)
print(c1.wheel)  #通过实例对象，查找属性时，会先查找实例属性，实例属性不存在再查找类属性

c2 = Car(c_color="黑色", c_brand="Tesla", c_name="Model Y", c_price=260000)
print(c2)