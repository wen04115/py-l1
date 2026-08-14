class Book:
    def __init__(self,title, author, price, stock):
        
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __str__(self):
        return (f"图书名: {self.title} | 作者: {self.author} | 价格: {self.price} 库存: {self.stock}")

    def update_stock(self,stock=None):
        if stock is not None:
            self.stock=stock

class BookManagement:
    def __init__(self):
        self.book_list=[]

    def add_book(self):
        name=input("请输入图书名:")
        for s in self.book_list:
            if s.title ==name:
                print("图书存在，添加失败")
                return
        else:
                author=input("请输入作者:")
                price=int(input("请输入价格:"))
                new_stock=int(input("请输入库存:"))
                if price>0 and price<=1000 and new_stock>0 and new_stock<=1000:
                      book = Book(name, author, price, new_stock)   # 先创建 Book 对象
                      self.book_list.append(book)    
                      print("图书添加成功")
                else:
                    print("库存或价格不符合要求")         
    def update_stock(self):
        name=input("请输入图书名:")
        for s in self.book_list:
            if s.title ==name:
                print(f"当前信息: {s}")
                new_stock=int(input("请输入库存:"))
                if new_stock>0 and new_stock<=1000:
                    s.update_stock(new_stock)
                    print("库存更新成功")
                else:
                    print("库存不符合要求")
                return
        else:
                print("未找到该图书")     
    def delete_book(self):
        name=input("请输入图书名:")
        for s in self.book_list:
            if s.title ==name:
                self.book_list.remove(s) 
                print("删除成功")
                return  
        else:    
                print("删除失败 未找到该图书")  
    def query_book(self):
        name=input("请输入图书名:")
        for s in self.book_list:
            if s.title ==name:
                print(f"当前信息: {s}")
                return
        else:
                print("未找到该图书")  
    def list_book(self):
        for s in self.book_list:
            print(s)
    def run(self):
         print("欢迎使用图书管理系统 1.0") 
         while True:
            print()
            print("#" * 8)
            print("#1.添加图书 2.修改库存 3.删除图书 4.查询图书 5.展示所有 6.退出系统 #")
            print("#" * 8)

            choice = input("请选择要执行的功能,输入1-6: ")

            match choice:
                case "1":                   
                    self.add_book()
                case "2":
                    self.update_stock()
                case "3":
                    self.delete_book()
                case "4":
                    self.query_book()
                case "5":
                    self.list_book()
                case "6":
                    print("退出系统")
                    break
                case _:
                    print("输入错误 请输入1-6")

if __name__ == "__main__":
    book_management = BookManagement()
    book_management.run()