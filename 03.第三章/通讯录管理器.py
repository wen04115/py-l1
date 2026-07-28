menu="""
   ===== 通讯录管理器 =====
1. 添加联系人
2. 查看所有联系人
3. 查找联系人
4. 修改电话
5. 删除联系人
6. 退出
========================  
"""
phone_card={}
print(menu)
while True:
   choice=input("请选择操作(1-6):")
   match choice:
     case "1":
        name=input("请输入姓名:")
        if name in phone_card:
            print("联系人已存在")
        else:
            number=input("请输入手机号:")
            phone_card[name] ={"电话": number}   
            print(f" ✅ 添加成功 {name}:{number}")
     case "2":
        if not phone_card:
            print("通讯录为空")
        else:  
            for name,info in  phone_card.items(): 
                print(f"联系人: {name} 电话:{info['电话']}")
     case "3":
        name=input("请输入姓名:")
        if name in phone_card:
            print(f"姓名:{name} 号码：{phone_card.get(name)["电话"]}")
        else:
            print("❌ 联系人不存在")
     case "4":
        name=input("请输入姓名:")
        if name in phone_card:
          number=input("请输入手机号")
          phone_card[name] ={"电话": number}
          print(f"✅ 修改成功 {name}:{number}")
        else:
           print("❌ 联系人不存在")    
     case "5":
        name=input("请输入姓名:")
        if name in phone_card:
           del phone_card[name]
           print("删除成功")
        else:
           print("❌ 联系人不存在")    
     case "6":
        print("退出")
        break
     case _:
        print("数字编码输入错误")