import json
class Member:
    def __init__(self,card_id,name,password):
        self.card_id = card_id
        self.name =name
        self.__password =password
        self.borrowed_books=[]

    def borrow_book(self,book):  #借书，加了book参数 
        if  len(self.borrowed_books) >= self.get_max_books():
            print("借阅失败,达到上限")
            return False
        if book.borrow_book():
            self.borrowed_books.append(book)
            print(f"借阅成功: {book.title}")
            return True
        print("借阅失败,库存不足")
        return False 

    def return_book(self, book):          # ④ 还书
        if book in self.borrowed_books:
            book.return_book()            # 委托图书加库存
            self.borrowed_books.remove(book)
            print(f"归还成功: {book.title}")
        else:
            print("归还失败，你没借这本书")     

    def get_borrowed_books(self):         # ⑤ 查看借阅：出示借阅列表
        return self.borrowed_books

    def get_password(self):  #登录用 出示密码
        return self.__password 

    def get_max_books(self): #借书用 ，拿上限，父类先空着，子类重写
        pass             

class NormalMember(Member):
    def get_max_books(self):
        return 3

class VIPMember(Member):
    def  __init__(self,card_id, name, password,level):
        super().__init__(card_id, name, password)
        self.level =level

    def get_max_books(self):
        
        return 6 + self.level

class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_num = total_num
        self.available_num = total_num      # 可用库存，初始 = 总数
    
    def borrow_book(self):   #借，减库存
        if self.available_num>0:
            self.available_num -=1
            return True
        return False    
 
    def return_book(self):
        self.available_num +=1

    def get_available_num(self):
        return self.available_num 

class BookManage:
    def __init__(self):
        self.books ={}  #编号  BOOK对象
        self.members = {}  #卡号  MEMBER对象
        self.current_member = None  #登录成功之后存这里
        self.load_data()  #创建对象时自动加载JSON

    def load_data(self):
        #加载图书
        with open(r"06.第六章/book/books.json","r",encoding="utf-8") as f:
            books_data =json.load(f)
        for book in books_data:
            self.books[book["编号"]] = Book(
                book["编号"], book["标题"], book["作者"], book["数量"]
            )
        #加载会员    
        with open(r"06.第六章/book/members.json","r",encoding="utf-8") as f:
            members_data =json.load(f)
            for member in members_data:
                if member["卡号"].startswith("N"):
                  self.members[member["卡号"]] = NormalMember(
                    member["卡号"], member["姓名"], member["密码"]
                  )
                elif member["卡号"].startswith("V"):
                    self.members[member["卡号"]] = VIPMember(
                      member["卡号"], member["姓名"], member["密码"], member["会员等级"]
                  )


    def Member_login(self):
        card_id=input("请输入会员卡")
        password=input("请输入密码")

        if card_id not in self.members:
            print("登录失败,卡号不存在")
            return False

        member = self.members[card_id] #从字典里取出对象
        if member.get_password() == password:
            self.current_member = member
            print("登录成功")
            return True
        print("登录失败,密码错误")
        return False    

    def borrow_book(self):
        if self.current_member is None:
            print("请先登录")
            return
        # 1. 展示书单
        for book in self.books.values():
           print(f"编号:{book.book_id}, 标题:{book.title}, 库存:{book.get_available_num()}")
        # 2. 收编号
        book_id = input("请输入要借阅的图书编号:")
        if book_id not in self.books:
          print("图书编号不存在")
          return
        # 3. 委托会员去借（会员自己登记 + 书自己减库存）
        self.current_member.borrow_book(self.books[book_id])    
    def return_book(self):
        if self.current_member is None:
           print("请先登录")
           return
        borrowed = self.current_member.get_borrowed_books()
        if not borrowed:
            print("您没有借阅任何图书")
            return
        for book in borrowed:
            print(f"编号:{book.book_id}, 标题:{book.title}")
        book_id = input("请输入要归还的图书编号:")
        if book_id not in self.books:
           print("图书编号不存在")
           return
        self.current_member.return_book(self.books[book_id])
    def ask_book(self): 
        if self.current_member is None:
          print("请先登录")
          return
        borrowed = self.current_member.get_borrowed_books()
        if not borrowed:
           print("您没有借阅任何图书")
        else:
           print("【我的借阅】")
        for book in borrowed:
            print(f"编号:{book.book_id}, 标题:{book.title}")       
    def run(self):
        # 启动先登录，登录失败就一直重试，成功后才显示菜单
        while not self.Member_login():
           pass
        while True:
           print("""
                         菜单
               1. **会员登录**：凭卡号 + 密码校验登录，登录成功后方可操作系统
               2. **借书**：仅可借阅库存有余量的图书
               3.**还书**：归还已借阅的图书
               4.**查看我的借阅**：展示本人当前已借阅的全部图书列表
               5.**退出系统**：结束程序使用
""") 
           choice=input("请输入操作编号:")
           match choice:
              case "1": 
                self.Member_login()
              case "2":
                self.borrow_book()
              case "3":
                self.return_book()
              case "4":
                self.ask_book()
              case  "5":
                   print("退出系统")
                   break  
              case _:   
                print("输入数字编码错误，请重新输入:")      

if __name__== "__main__":
    book=BookManage()
    book.run()