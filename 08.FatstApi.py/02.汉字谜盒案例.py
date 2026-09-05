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
import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from fastapi import Header

from starlette.responses import JSONResponse
from fastapi import Request
from sqlalchemy import create_engine, text

# ===== PostgreSQL 连接 =====
引擎 = create_engine("postgresql+psycopg2://postgres:123456@localhost:5432/hanzi_box")

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

#JWT鉴权
SECRET_KEY = "wode_mimi_yaoshi_2026_hanzibox_8888" 
ALGORITHM ="HS256" 
TOKEN有效期 = timedelta(hours=24)
密码加密器 = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

class RegisterRequest(BaseModel):
    username: str
    password: str  

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

       #2.写入 PostgreSQL
       with 引擎.connect() as 连接:
           连接.execute(
               text("INSERT INTO sessions (session_id, messages) VALUES (:sid, :msg)"),
               {"sid": session_id, "msg": json.dumps({"messages": []}, ensure_ascii=False)}
           )
           连接.commit()

       #3.返回数据
       return {"code":200, "message":"创建会话成功","data":session_id}

@app.get("/api/sessions")
def get_sessions():
    # 从 PostgreSQL 查所有会话
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
     数据 = row[0] if not isinstance(row[0], str) else json.loads(row[0])
     return {"code": 200, "message": "获取成功", "data": 数据}

#删除对话
@app.delete("/api/sessions/{session_id}")
def del_session(session_id:str):
    with 引擎.connect() as 连接:
        连接.execute(text("DELETE FROM sessions WHERE session_id = :sid"), {"sid": session_id})
        连接.commit()
    return {"code": 200, "message": "删除成功", "data": None} 

# 注册
@app.post("/api/register")
def register(请求: RegisterRequest):
    with 引擎.connect() as 连接:
        row = 连接.execute(text("SELECT id FROM users WHERE username = :u"),
                           {"u": 请求.username}).fetchone()
        if row:
            return {"code": 400, "message": "用户名已存在", "data": None}
        密码哈希 = 密码加密器.hash(请求.password)
        连接.execute(text("INSERT INTO users (username, password) VALUES (:u, :p)"),
                     {"u": 请求.username, "p": 密码哈希})
        连接.commit()
    return {"code": 200, "message": "注册成功", "data": None}

# 登录
@app.post("/api/login")
def login(请求: RegisterRequest):
    with 引擎.connect() as 连接:
        row = 连接.execute(text("SELECT id, username, password FROM users WHERE username = :u"),
                           {"u": 请求.username}).fetchone()
    if row is None or not 密码加密器.verify(请求.password, row[2]):
        return {"code": 400, "message": "用户名或密码错误", "data": None}
    payload = {"sub": row[1], "exp": datetime.now(timezone.utc) + TOKEN有效期}
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return {"code": 200, "message": "登录成功", "data": token}

# 校验 token 的工具函数
def 校验token(Authorization: str = Header(None)):
    if not Authorization:
        return None
    try:
        token = Authorization.replace("Bearer ", "")
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]
    except jwt.PyJWTError:
        return None


#与AI交互
@app.post("/api/chat")
def chat(request:ChatRequest, Authorization: str = Header(None)):
    用户名 = 校验token(Authorization)
    if 用户名 is None:
        return {"code": 401, "message": "未登录，请先登录获取 token", "data": None}
    
    with 引擎.connect() as 连接:
        #读历史
        row = 连接.execute(
            text("SELECT messages FROM sessions WHERE session_id = :sid"),
            {"sid": request.session_id}
        ).fetchone()
        session_data = (json.loads(row[0]) if isinstance(row[0], str) else row[0]) if row else {"messages": []}
        messages = session_data["messages"]

        #拼用户消息+调OLLAMA
        messages.append({"role":"user","content":request.message})
        response=requests.post(
            "http://localhost:11434/api/chat",
            json={"model":"qwen2.5:3b", "messages": messages, "stream": False},
            timeout=60
        )
        content=response.json()["message"]["content"]

        #存AI回复+写回数据库
        messages.append({"role":"assistant","content":content})
        连接.execute(
            text("UPDATE sessions SET messages = :msg WHERE session_id = :sid"),
            {"msg": json.dumps(session_data, ensure_ascii=False), "sid": request.session_id}
        )
        连接.commit()

    #返回
    return {"code":200,"message":"请求成功","data":content}

#全局异常处理（临时：返回具体错误信息方便调试）
@app.exception_handler(Exception)
def handler_exception(request: Request, exc: Exception):
    import traceback
    错误详情 = traceback.format_exc()
    logging.error(f"处理异常, 请求路径: {request.url}, 异常: {exc}\n{错误详情}")
    return JSONResponse(
        status_code=500,
        content={"code": 500, "message": f"服务器内部错误: {exc}", "data": None}
    )


#启动项目
if __name__ =="__main__" :
       import uvicorn
       uvicorn.run(app,host="127.0.0.1",port=8000,reload=False)    
     