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
from sqlalchemy import create_engine, text

BASE_DIR = Path(__file__).resolve().parent
INDEX_HTML = BASE_DIR / "static" / "index.html"
SESSION_DIR = BASE_DIR / "sessions"

#日志配置
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s -%(message)s"
)
# ===== 新增：PostgreSQL 连接（把「你的密码」换成你的） =====
引擎 = create_engine("postgresql+psycopg2://postgres:123456@localhost:5432/hanzi_box")

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
    session_id = generate_session_id()
    with 引擎.connect() as 连接:
        连接.execute(
            text("INSERT INTO sessions (session_id, messages) VALUES (:sid, :msg)"),
            {"sid": session_id, "msg": json.dumps({"messages": []}, ensure_ascii=False)}
        )
        连接.commit()
    return {"code": 200, "message": "创建会话成功", "data": session_id}

#会话列表
@app.get("/api/sessions")
def get_sessions():
    with 引擎.connect() as 连接:
        rows = 连接.execute(text("SELECT session_id FROM sessions ORDER BY id DESC")).fetchall()
    return {"code": 200, "message": "获取成功", "data": [row[0] for row in rows]}


#加载会话
@app.get("/api/sessions/{session_id}")
def load_sessions(session_id: str):
    with 引擎.connect() as 连接:
        row = 连接.execute(
            text("SELECT messages FROM sessions WHERE session_id = :sid"),
            {"sid": session_id}
        ).fetchone()
    if row is None:
        return {"code": 404, "message": "会话不存在", "data": None}
    return {"code": 200, "message": "获取成功", "data": json.loads(row[0])}


#删除对话
@app.delete("/api/sessions/{session_id}")
def del_session(session_id: str):
    with 引擎.connect() as 连接:
        连接.execute(text("DELETE FROM sessions WHERE session_id = :sid"), {"sid": session_id})
        连接.commit()
    return {"code": 200, "message": "删除成功", "data": None}
    

#与AI交互
@app.post("/api/chat")
def chat(request: ChatRequest):
    with 引擎.connect() as 连接:
        row = 连接.execute(
            text("SELECT messages FROM sessions WHERE session_id = :sid"),
            {"sid": request.session_id}
        ).fetchone()
        session_data = json.loads(row[0]) if row else {"messages": []}
        messages = session_data["messages"]

        messages.append({"role": "user", "content": request.message})
        response = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": "qwen2.5:3b", "messages": messages, "stream": False},
            timeout=60
        )
        content = response.json()["message"]["content"]
        messages.append({"role": "assistant", "content": content})

        连接.execute(
            text("UPDATE sessions SET messages = :msg WHERE session_id = :sid"),
            {"msg": json.dumps(session_data, ensure_ascii=False), "sid": request.session_id}
        )
        连接.commit()
    return {"code": 200, "message": "请求成功", "data": content}


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
     