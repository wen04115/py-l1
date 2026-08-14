import json

#写入json数据文件
# user = {
#     "name" :"小明",
#     "age" : 18,
#     "gender" : "男",
#     "hobbies" : ["reading","swiming"]
# }
#序列化
# with open(r"C:\Users\hp\Desktop\json入门.txt","w",encoding="utf-8") as f:
#     json.dump(user,f,ensure_ascii= False,indent=2)  #把user对象转换成有序的json字符串写到f这个文件中  
    #ensure_ascii= False把中文乱码以中文的方式输出   ensure_ascii= True 确保所有的数据以ASCII码的形式输出
    # indent=2缩进两个字符

#反序列化
#读取json数据文件
with open(r"C:\Users\hp\Desktop\json入门.txt","r",encoding="utf-8") as f:    
    user=json.load(f)  #将文件中的字符串自动加载出来成对象
    print(user)