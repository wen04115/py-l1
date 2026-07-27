num_list=[]
while True:
    print("\n=== 待办事项管理器 ===")
    print("1. 添加任务")
    print("2. 查看所有任务")
    print("3. 删除任务")
    print("4. 标记任务完成")
    print("0. 退出")
    num=int(input("请输入数字进行操作:"))
    if num==1:
        if len(num_list)==0:
          print("请输入任务内容:")
          num_list.append(input())
        else:
          print("当前列表总长度为:",len(num_list))
          i=int(input("请输入要添加的位置:")) 
          if 1<=i and i<=len(num_list):
            string=input("请输入要添加的内容:")
            num_list.insert(i-1,string)
            print("任务添加完成")
          else:
            print("输入的编号不符合列表范围")
            continue  
    elif num==2:
        print("查看所有任务")
        if len(num_list)==0:
           print("暂无任务")
        else:
            print(num_list)    
    elif num==3:
        print("删除任务")
        if len(num_list)==0:
           print("暂无任务可操作")
        else:
            print("当前列表总长度为:",len(num_list))
            x=int(input("请输入要删除的位置:"))
            if x>=1 and x<=len(num_list):
              num_list.pop(x-1)
              print("任务删除完成")
            else:
              print("输入的编号不符合列表范围")
              continue
    elif num==4:
        print("当前列表总长度为:",len(num_list))
        y=int(input("请输入要标记的位置:"))
        if y>=1 and y<=len(num_list):
              num_list[y-1]="[✓]"+num_list[y-1]
              print("标记任务完成")
        else:
              print("输入的编号不符合列表范围")
              continue
    elif num==0:
        print("退出")
        break                   
    else:
        print("输入错误")   