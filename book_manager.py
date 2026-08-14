from cgi import print_exception
import json
from multiprocessing import AuthenticationError
from re import S

class Book:
    def __init__(self,title,author,price,stock):
        self.title=title
        self.author=author
        self.price=price
        self.stock=stock
        

    def __str__(self):
        return f"书名: {self.title} | 作者: {self.author} | 价格: {self.price} | 库存: {self.stock}"

    def update_stock(self,stock=None):
        if stock is not None:
            self.stock=stock


class BookManagement:
    def __init__(self):
      self.book_list=[]

    def add_book(self):
        name=input("请输入图书名字:")
        for i in self.book_list:
            if i.title==name:
                print("该图书已存在，添加失败")
                return
        else:
           while True: 
            try:
                stock=int(input("请输入库存:"))
            except ValueError:
                  print("库存必须是数字")
                  continue    
            if stock>0 and stock<=9999:
                    author=input("请输入作者:")
                    price=input("请输入价格:")
                    book=Book(name,author,price,stock)
                    self.book_list.append(book)
                    print("添加成功")
                    break
            else:
                    print("库存数量不符合要求,请重新输入")

    def delete_book(self):
        name=input("请输入图书名字:")                    
        for i in self.book_list:
            if i.title==name:
                self.book_list.remove(i)
                print("该书已删除,操作成功")
                return 
        else:
                print("该书不存在")

    def update_stock(self):
        name=input("请输入图书名字:")
        for i in self.book_list:
            if i.title==name:
              try: 
                new_stock=int(input("请输入新库存:"))
              except ValueError:
                 print("库存必须是数字")
                 return
              if new_stock>0 and new_stock<=9999:
                    i.update_stock(new_stock)
                    print("库存修改成功")
                    return 
              else:
                    print("库存数量不符合要求,请重新输入")
                    return
        else:
            print("该书不存在，请重新输入")              

    def quary_book(self):
        name=input("请输入图书名字:")
        for i in self.book_list:
            if i.title==name:
                print(i)
                return
        else:
                print("图书不存在，请重新输入")

    def all_book(self):
        if not self.book_list:
          print("暂无图书")
          return
        for i in self.book_list:
           print(i)

    def save_to_file(self):
        data=[]
        for book in self.book_list:  
            data.append({
                "title" :book.title,
                "author" : book.author,
                "price": book.price, 
                "stock" : book.stock,
            })
        with open("books.json","w",encoding="utf-8") as f:
            json.dump(data,f,ensure_ascii=False,indent=2)   
        print("已保存到books.json")

    def load_from_file(self):
        try:
            with open("books.json","r",encoding="utf-8") as f:
                data=json.load(f)
            self.book_list=[]
            for item in data:
                book=Book(item["title"],item["author"],item["price"],item["stock"])
                self.book_list.append(book)
                print("已从books.json加载完毕")
        except FileNotFoundError:
            print("未找到books.json,将以空列表启动")                         
        

    def run(self):
        print("欢迎使用图书管理系统 1.0")
        self.load_from_file()
        while True:
            print("#" * 8)
            print("#1.添加图书 2.修改库存 3.删除图书 4.查询图书 5.展示所有 6.退出系统 #")
            print("#" * 8)
            try:
              choice=int(input("请输入操作按钮:"))
            except ValueError:
                print("请输入数字:")
                continue  
            match choice:
                case 1:
                    self.add_book()
                    self.save_to_file()
                case 2:
                    self.update_stock()
                    self.save_to_file() 
                case 3:
                    self.delete_book()
                    self.save_to_file()
                case 4:
                    self.quary_book()
                case 5:
                    self.all_book()
                case 6:
                    print("退出系统")
                    break
                case _:
                    print("数字输入错误，请重新输入") 

if __name__ ==  "__main__":
    bookmanagement=BookManagement()
    bookmanagement.run()                                                                                                       
