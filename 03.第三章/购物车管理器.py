shangpin_list=[]
price_list=[]
print("=== 购物车管理器 ===")
print("1. 添加商品")
print("2. 查看购物车")
print("3. 删除商品")
print("0. 退出")
while True:
    num=int(input(("请选择操作:")))
    if num==1:
        if len(shangpin_list)==0 and len(price_list)==0:
          shangpin=input("请输入商品名称:")
          shangpin_list.append(shangpin)
          price=input("请输入商品价格:")
          price_list.append(price)
          print(f"已添加: {shangpin_list} ({price_list}元)")
        else:
          print("当前列表长度是：",len(shangpin_list))  
          location=int(input("请输入要添加的位置:"))
          if location>=1 and location<=len(shangpin_list):
             shangpin=input("请输入商品名称:")
             shangpin_list.insert(location-1,shangpin)
             price=input("请输入商品价格:")
             price_list.insert(location-1,price)
             for k in range(len(shangpin_list)):
                 print(f"已添加: {shangpin_list[k]} ({price_list[k]}元)")
          else:
            print("输入编号有误，请重新输入")
            continue
    elif num==2:
        if (len(shangpin_list)!=0) and (len(price_list)!=0):
            print("购物车列表:")
            total=0
            for i in range(len(shangpin_list)):
                total+=float(price_list[i])
                print(f"{i+1}. {shangpin_list[i]} - {price_list[i]}元")
            print(f"总计:{total}元")
        else:
            print("🛒 购物车是空的")
    elif num==3:
        if (len(shangpin_list)!=0) and (len(price_list)!=0):
            print("购物车列表:")
            total=0
            for i in range(len(shangpin_list)):
                total+=float(price_list[i])
                print(f"{i+1}. {shangpin_list[i]} - {price_list[i]}元")
            j=int(input("请输入要删除的编号:"))
            if 1 <= j <= len(shangpin_list):
             z=shangpin_list[j-1]
             shangpin_list.pop(j-1)
             price_list.pop(j-1)
             print("🗑️ 已删除：",z)
        else:
            print("输入编号有误，请重新输入")
            continue        
    elif num==0:
         print("感谢使用，再见")
         break
    else:
        print("输入编号有误，请重新输入")     