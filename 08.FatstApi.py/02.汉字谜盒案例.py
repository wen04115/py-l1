from datetime import datetime
import json
import os
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles
from pathlib import Path
from typing import Any
import requests
import logging
from starlette.responses import JSONResponse
from fastapi import Request

BASE_DIR = Path(__file__).resolve().parent
INDEX_HTML = BASE_DIR / "static" / "index.html"
SESSION_DIR = BASE_DIR / "sessions"

#日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -%(message)s"
)

#创建FastAPI实例
app = FastAPI(title ="汉字谜盒")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
#挂载静态文件存放目录  第一个static是访问的路径以这个开头 第二个是静态资源文件所在的目录名 第三个随便写 换其他的名字也行

#创建会话存放的目录sessions
if not SESSION_DIR.exists():
    SESSION_DIR.mkdir()

#生成会话的标识
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

#数据模型
class ApiResponse(BaseModel):
    code:int
    message:str
    data:Any 

class ChatRequest(BaseModel):
    session_id:str
    message:str

#定义路径操作函数
@app.get("/")  
def root():
    logging.info("访问项目首页")
    return FileResponse(INDEX_HTML)

#创建对话
@app.post("/api/sessions")
def create_session():    
       logging.info("创建会话")
       #1.生成会话的标识(名字)
       session_id =generate_session_id()

       #2.组装会话信息，保存到文件
       session_data = {
        "current_session":session_id,
        "messages":[]
       }
       with open(SESSION_DIR / f"{session_id}.json", "w",encoding="utf-8") as f:
           json.dump(session_data,f,ensure_ascii=False,indent=2)

       #3.返回数据
       return {"code":200, "message":"创建会话成功","data":session_id}

@app.get("/api/sessions")
def get_sessions():
    # 列出会话目录里所有 .json 文件名
    session_dir = BASE_DIR / "sessions"
    if not session_dir.exists():
        return {"code": 200, "message": "获取成功", "data": []}
    session_ids = [f.stem for f in session_dir.glob("*.json")]
    session_ids.sort(reverse=True)  # 最新的在前
    return {"code": 200, "message": "获取成功", "data": session_ids}

#加载会话
@app.get("/api/sessions/{session_id}")
def load_sessions(session_id: str):
     json_file = SESSION_DIR / f"{session_id}.json"
     with open(json_file,"r",encoding="utf-8") as f:
       session_data=json.load(f)

     return {"code": 200, "message": "获取成功", "data": session_data}

#删除对话
@app.delete("/api/sessions/{session_id}")
def del_session(session_id:str):     
    json_file = SESSION_DIR / f"{session_id}.json"
    if json_file.exists():
        json_file.unlink()
    return {"code": 200, "message": "删除成功", "data": None}    

#与AI交互
@app.post("/api/chat")
def chat(request:ChatRequest):
    #读历史
    json_file=SESSION_DIR / f"{request.session_id}.json"
    with open(json_file,"r",encoding="utf-8") as f:
        session_data=json.load(f)
    messages= session_data["messages"]  

    #拼用户消息+调OLLAMA
    messages.append({"role":"user","content":request.message}) 
    response=requests.post(
        "http://localhost:11434/api/chat",
        json={"model":"qwen2.5:3b", "messages": messages, "stream": False},
        timeout=60
    )
    content=response.json()["message"]["content"]

    #存AI回复+写回
    messages.append({"role":"assistant","content":content})
    with open(json_file,"w",encoding="utf-8") as f:
        json.dump(session_data,f,ensure_ascii=False,indent=2)
    
    #返回
    return {"code":200,"message":"请求成功","data":content}

#全局异常处理
@app.exception_handler(Exception)
def handler_exception(request: Request, exc: Exception):
    logging.error(f"处理异常, 请求路径: {request.url}, 异常: {exc}")
    return JSONResponse(
        status_code=500,
        content={"code": 500, "message": "服务器内部错误", "data": None}
    )


#启动项目
if __name__ =="__main__" :
       import uvicorn
       uvicorn.run(app,host="127.0.0.1",port=8000,reload=False)    
     