# 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5．退出购物车
shopping_card={}
# 制作菜单
print("欢迎使用购物车管理系统")
menu="""
######## 购物车系统 ########
#       1.添加购物车        #
#       2.修改购物车        #
#       3.删除购物车        #
#       4.查询购物车        #
#       5.退出购物车        #   
############################ 
"""
print(menu)

#执行具体操作
while True:
 choice=input("请选择要执行的操作(1-5):")
 match choice:
    case "1" :#添加购物车
      goods_name=input("请输入商品名称:")    
      if goods_name not in shopping_card:  
        goods_price=input("请输入商品价格:")
        goods_count=input("请输入商品数量:")
        shopping_card[goods_name] = f"商品价格:{goods_price},商品数量:{goods_count}"
      else:
        print("该商品已添加，请重新输入")
    case "2" :#修改购物车
        goods_name=input("请输入商品名称:")
        if goods_name  in shopping_card:
             goods_price=input("请输入商品价格:")  
             goods_count=input("请输入新的商品数量:")
             shopping_card[goods_name] = f"商品价格:{goods_price},商品数量:{goods_count}"
        else:
          print("没有该商品，请重新输入")
    case "3" :#删除购物车
        goods_name=input("请输入商品名称:")
        if goods_name  in shopping_card:
             shopping_card.pop(goods_name)
             print("删除成功")
        else:
          print("没有该商品，请重新输入")
    case "4" :#查询购物车
          if not shopping_card:
            print("购物车为空")
          else:  
            for name, info in shopping_card.items():
             print(f"商品名称：{name},{info}") 
    case "5" :#退出购物车
          print("退出购物车")
          break
    case _ :  #匹配其他所有情况
        print("输入数字不正确，请重新输入")
          
