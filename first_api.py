
import json
from typing import Dict
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel   #从fastapi模块导入FastAPI功能

app=FastAPI()   #创建应用，名字必须叫app uvicorn要找到他
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

riddles:Dict[int,dict]={}   #定义字典存谜题
FILE="riddle.json"

next_id=1  #给每个新谜题发不重复编号，从 1 开始，每存一个 +1

try:
    with open(FILE,"r",encoding="utf-8") as f:
        riddles = {int(k): v for k, v in json.load(f).items()}      # 读出来直接转 int 键
        next_id = max(riddles.keys(), default=0) + 1                 # 现在 keys() 全是 int，直接用

        
except FileNotFoundError:
    print("文件不存在")

def save():
    with open(FILE,"w",encoding="utf-8") as f:
        json.dump(riddles,f,ensure_ascii=False)

class RiddleCreate(BaseModel): #定义请求体模型#pydantic写法，只声明字段和类型，FastAPI自动校验请求体
    question:str   #规定post过来的json类型
    answer:str

@app.get("/")   #装饰器 把下面的函数绑到GET/路由
def root():
    return {"msg":"汉字秘盒API启动成功"}

@app.post("/api/riddles")  #装饰器：把下面这个函数绑到 POST /api/riddles 这个地址，用户往这发post就执行她
def create_riddle(riddle: RiddleCreate):
    global next_id  #在函数内部，告知 Python 解释器“这个变量不是局部变量，请到全局作用域中去查找和操作它”。
    riddles[next_id]={"question":riddle.question,"answer":riddle.answer}
    next_id+=1
    save()
    return {"id":next_id-1,"question":riddle.question,"answer":riddle.answer}

@app.get("/api/riddles")
def list_riddles():
    return [{"id":k,**v} for k,v in riddles.items()]


@app.get("/api/riddles/{riddle_id}")     # 路径参数 {riddle_id}
def get_riddle(riddle_id: int):
    if  riddle_id not in riddles:
        raise HTTPException(status_code=404, detail="谜题不存在")  
    return riddles[riddle_id]

@app.delete("/api/riddles/{riddle_id}")
def delete_riddle(riddle_id: int): 
    if riddle_id not in riddles:
        raise HTTPException(status_code=404, detail="谜题不存在")            
    riddles.pop(riddle_id)
    save()
    return {"msg":"删除成功","id":riddle_id}
    