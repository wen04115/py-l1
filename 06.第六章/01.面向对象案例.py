# 社区图书馆图书管理系统需求提取

## 项目概述

# 采用面向对象编程思想，开发社区简易图书管理系统，区分**普通会员、VIP 会员**两类用户，二者借书额度权限不同；包含登录、借还书、查阅借阅记录、退出整套流程。
#
# ## 一、核心功能清单

# 1. **会员登录**：凭卡号 + 密码校验登录，登录成功后方可操作系统
# 2. **借书**：仅可借阅库存有余量的图书
# 3. **还书**：归还已借阅的图书
# 4. **查看我的借阅**：展示本人当前已借阅的全部图书列表
# 5. **退出系统**：结束程序使用

# ## 二、借阅权限规则

# 1. 普通会员：单次最多可借阅 **3 本**
# 2. VIP 会员：最大可借数量 = 6 + VIP 等级；VIP 等级默认初始为 1

# ## 三、约束注意事项

# 1. 必须卡号、密码全部校验正确，登录成功后，才能使用系统所有业务功能
# 2. 两种场景无法借书：
#    - 目标图书库存余量不足
#    - 当前会员已借书数量，达到自身最大借阅上限

# ## 面向对象设计拆解（配套实现思路）

# 1. **图书类 Book**：属性：书名、库存数量；方法：减少库存、归还增加库存
# 2. **会员父类 Member**：属性：卡号、密码、已借图书列表；方法：登录校验、借书、还书、查看借阅记录、获取最大可借数量
# 3. **普通会员子类 OrdinaryMember**：继承 Member，重写最大借阅数（固定 3 本）
# 4. **VIP 会员子类 VipMember**：继承 Member，属性新增 vip 等级；重写最大借阅数（6 + 等级）
# 5. **图书馆系统类 LibrarySystem**：统一管理图书、会员，搭建菜单交互界面

#书籍类
from abc import ABC,abstractmethod
import json

class Book:
    def __init__(self,book_id,title,author,total_num) :
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = total_num #总数量
        self.available_num=total_num #可用数量一开始默认等于总数量

    def borrow_book(self):  #借阅书籍 可用数量减一
        if  self.available_num>0:
            self.available_num-= 1
            return True
        return False    

    def return_book(self):  #归还书籍 可用数量加一
        self.available_num+= 1    

    def get_available_num(self): #获取可用数量
        return self.available_num
#抽象类：是一种只能被继承，不能被直接实例化的类，作用就是规定子类必须要实现哪些方法，强制子类必须遵守统一的代码规范
#python中的抽象类，需要被abc类的ABC继承  ABC ：Abstract Base Class
#会员类
class Member(ABC):
    def __init__(self,member_id,name,password) :
        self.memeber_id =member_id  #会员卡号
        self.name =name
        self.__password =password
        self.__borrowed_books=[]  #会员借阅的书籍列表

    def borrow_book(self,book):  #借阅书籍
        #判断当前会员借阅数量是否达到最大限制   
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅失败，您的借阅数量已达到最大限制")
            return False
        
        #判断书籍是否可以借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name}已成功借阅图书 {book.title}")
            return True
        else:
            print(f"借阅失败，图书{book.title}已被借完")
            return False    

    def return_book(self,book):  #归还书籍
        #判断当前会员是否借了书籍
        if book in self.__borrowed_books:
            #还书
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name}已成功归还图书{book.title}")
        else:
            print(f"归还失败，您没有借阅图书{book.title}")  

    def get_password(self): 
        return self.__password

    def get_borrowed_books(self):
        return self.__borrowed_books                     

    @abstractmethod
    def  get_max_books(self):  #获取会员最大借阅数量 ，需要在子类中实现      
        pass


#普通会员类
class NormalMember(Member):
    def  get_max_books(self):  #获取会员最大借阅数量 ，需要在子类中实现      
       return 3
#VIP会员类 
class VIPMember(Member):
       def __init__(self,member_id,name,password,vip_level):
            super().__init__(member_id,name,password)
            self.vip_level =vip_level  #会员等级

       def  get_max_books(self):   
            return 6+self.vip_level

#图书馆管理系统
class LibrarySystem():
    def __init__(self): 
        self.books={} #书籍 {"AI001":Book对象,"AI002":Book对象} 
        self.members={}  #会员 {"N001":Member对象,"N002":Member对象}
        self.current_member: Member|None =None #当前登录会员 可以是Member或None类型
        #加载数据（书籍，会员）
        self.load_books_data()
        self.load_members_data() 

    def load_books_data(self):
        #加载data/books.json中的数据
        with open(r"06.第六章\book\books.json","r",encoding="utf-8") as f:
            books_data =json.load(f)
            for book in books_data:
                self.books[book['编号']] =Book(book['编号'],book['标题'],book['作者'],book['数量'])
            print("加载数据成功")   

    def load_members_data(self):               
        #加载data/members.json中的数据
        with open(r"06.第六章\book\members.json","r",encoding="utf-8") as f:
            members_data =json.load(f)
            for member in members_data:
                if member['卡号'].startswith('N'):
                    self.members[member['卡号']] =NormalMember(member['卡号'],member['姓名'],member['密码'])
                elif member['卡号'].startswith('V'):
                    self.members[member['卡号']] =VIPMember(member['卡号'],member['姓名'],member['密码'],member['会员等级'])    
            print("加载会员数据成功")

    def login(self):#登录
       while True: 
        print("【登录】")
        member_id=input("请输入会员卡号:")
        password =input("请输入会员密码:")

        #判读会员卡号是否存在
        if  member_id not in self.members:
            print("登录失败，会员卡号不存在")
            continue 

        #判断密码是否正确
        member=self.members[member_id]
        if member.get_password() ==password:
            print("登录成功")
            self.current_member =member
            return True
        else:
            print("登录失败,密码错误")
            continue

    def borrow_book(self): #借阅图书
        #1.展示当前图书馆的图书列表
         for book in self.books.values():
             print(f"编号:{book.book_id},标题:{book.title},作者:{book.title},总数:{book.total_num},可用:{book.get_available_num()}")
        
        #2.获取用户输入的图书编号,执行借书操作
         book_id =input("请输入要借阅的图书编号:")
         if book_id not in self.books:
            print("借阅失败，图书编号不存在")
            return
         self.current_member.borrow_book(self.books[book_id])    

    def return_book(self):
        #1.展示当前会员的借阅列表
        borrowed_books =self.current_member.get_borrowed_books()
        print("【已经借阅的图书列表:】")
        for book in borrowed_books:
            print(f"编号:{book.book_id},标题:{book.title}")

        #2.获取用户输入的图书编号，执行还书操作
        book_id =input("请输入要归还的图书编号:")
        if book_id not in self.books:
            print("还书失败，图书编号不存在")
            return
        self.current_member.return_book(self.books[book_id])

    def show_borrowed_books(self):
        borrowed_books=self.current_member.get_borrowed_books()
        if len(borrowed_books)> 0:
            print("【已经借阅的图书列表:】")
            for book in borrowed_books:
                print(f"编号:{book.book_id},标题:{book.title}")
        else:
            print("您没有借阅任何图书")        



    def run(self):
        if self.login():
            while True:
                print("\n1.借阅图书")
                print("2.归还图书")
                print("3.查看借阅")
                print("4.退出系统")

                choice=input("请选择操作(1-4):")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统")
                        break
                    case _:
                        print("无效的选项，请重新选择:") 

if __name__ == "__main__":
    system = LibrarySystem()
    system.run()
