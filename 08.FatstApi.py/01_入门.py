from fastapi import FastAPI

#创建FASTAPI实例
app=FastAPI()

#定义API接口,该函数返回值表示API接口的返回的数据，接口访问路径为/  访问方式为get
@app.get("/")
def root():
    return {"message":"Hello World"}

#定义API接口 
@app.get("/users")
def get_users():
    return[
        {"id":1, "name": "张三"},
        {"id":2, "name": "李四"},
        {"id":3, "name": "王五"},
    ]

#启动服务 uvicorn:Python中的轻量级Web服务器
if __name__ =="__main__" :
       import uvicorn
       uvicorn.run(app,host="127.0.0.1",port=8000)  #第一个参数是要启动的实例名 第二个是谁可以访问 第三个是端口号
       #127.0.0.1是只能本机访问  0.0.0.0是可以所有人访问