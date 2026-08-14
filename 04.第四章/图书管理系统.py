class Book:
    def __init__(self, title, author, price, stock):
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"书名: {self.title} | 作者: {self.author} | 价格: {self.price} | 库存: {self.stock}"

    def update_stock(self, stock=None):
        if stock is not None:
            self.stock = stock


class BookManagement:

    def __init__(self):
        self.book_list = []

    def add_book(self):
        name = input("请输入书名:")

        for s in self.book_list:
            if s.title == name:
                print("该书已存在,添加失败")
                return

        author = input("请输入作者:")
        price = int(input("请输入价格:"))
        stock = int(input("请输入库存:"))
        if 0 <= price <= 1000 and 0 <= stock <= 9999:
            book = Book(name, author, price, stock)
            self.book_list.append(book)
            print("添加成功")
        else:
            print("价格必须在0-1000之间,库存必须在0-9999之间")

    def update_stock(self):
        name = input("请输入书名:")
        for s in self.book_list:
            if s.title == name:
                print(f"当前信息: {s}")
                new_stock = int(input("请输入新的库存:"))
                if 0 <= new_stock <= 9999:
                    s.update_stock(new_stock)
                    print("库存修改成功")
                    print(f"修改后信息: {s}")
                    return
                else:
                    print("库存必须在0-9999之间,修改失败")
                    return
        print("未找到该书，修改失败")

    def del_book(self):
        name = input("请输入书名:")
        for s in self.book_list:
            if s.title == name:
                self.book_list.remove(s)
                print("删除成功")
                return
        print("没有该图书，删除失败")

    def query_book(self):
        name = input("请输入书名:")
        for s in self.book_list:
            if s.title == name:
                print(f"图书信息: {s}")
                return
        print("未找到该书")

    def all_book(self):
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
                    self.del_book()
                case "4":
                    self.query_book()
                case "5":
                    self.all_book()
                case "6":
                    print("退出系统")
                    break
                case _:
                    print("输入数字有误")


if __name__ == "__main__":
    bookmanagement = BookManagement()
    bookmanagement.run()
