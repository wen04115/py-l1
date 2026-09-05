import logging
import json
from typing import Dict
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel   #从fastapi模块导入FastAPI功能

app=FastAPI()   #创建应用，名字必须叫app uvicorn要找到他
from fastapi.middleware.cors import CORSMiddleware

logging.basicConfig( #制定日志规则
    level=logging.INFO,  #必须INFO以上的等级才能写入日志 
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s', #每个日记的长相:时间 [级别] 谁记得:内容
    handlers=[
        logging.FileHandler("riddle_api.log",encoding="utf-8"), #抄一份写进文件riddle_apo.log，长期保存
        logging.StreamHandler()  #抄一份打到终端  实时看
    ]
)

logger = logging.getLogger("first_api") # getLogger("first_api") = 领一台频道为 first_api 的对讲机（全局只有一台）
#logger.info(...) = 对着它喊话；喊的话会按 basicConfig 定的规矩（分级+格式）打到终端和文件，并自动署名 first_api

app.add_middleware(    
    CORSMiddleware,   #跨域访问，专门用来处理浏览器同源策略
    allow_origins=["http://localhost:5173"], #允许哪些前端访问后端 :允许这个地址访问
    allow_credentials=True, #允许前端携带身份凭证
    allow_methods=["*"],  #允许所有 HTTP 请求方法 get put等
    allow_headers=["*"],  #允许前端带任意请求头
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
    logger.info("GET/called")
    return {"msg":"汉字秘盒API启动成功"}

@app.post("/api/riddles")  #装饰器：把下面这个函数绑到 POST /api/riddles 这个地址，用户往这发post就执行她
def create_riddle(riddle: RiddleCreate):
    global next_id  #在函数内部，告知 Python 解释器“这个变量不是局部变量，请到全局作用域中去查找和操作它”。
    logger.info(f"POST /api/riddles: question={riddle.question}, answer={riddle.answer}") #logger.info 正式请求记录
    riddles[next_id]={"question":riddle.question,"answer":riddle.answer}
    next_id+=1
    save()
    logger.debug(f"created riddle id={next_id-1}")  #日志对象.日志等级  logger.debug调试细节
    return {"id":next_id-1,"question":riddle.question,"answer":riddle.answer}

@app.get("/api/riddles")
def list_riddles():
    logger.info(f"GET /api/riddles: returning {len(riddles)} riddles") 
    #有人调这个接口时，记账员记一笔：2026-09-05 16:10 [INFO] first_api: GET /api/riddles: returning 3 riddles
    #f"..." 是 f-string把 {len(riddles)} 这种变量的值塞进字符串，所以你看到的是实际数字，不是 {len(riddles)} 这串字
    return [{"id":k,**v} for k,v in riddles.items()]


@app.get("/api/riddles/{riddle_id}")     # 路径参数 {riddle_id}
def get_riddle(riddle_id: int):
    logger.info(f"GET /api/riddles/{riddle_id}")
    if  riddle_id not in riddles:
        logger.warning(f"riddle {riddle_id} not found")
        raise HTTPException(status_code=404, detail="谜题不存在")  
    return riddles[riddle_id]

@app.delete("/api/riddles/{riddle_id}")
def delete_riddle(riddle_id: int): 
    logger.info(f"DELETE /api/riddles/{riddle_id}")
    if riddle_id not in riddles:
        logger.warning(f"riddle {riddle_id} not found for delete")
        raise HTTPException(status_code=404, detail="谜题不存在")            
    riddles.pop(riddle_id)
    save()
    logger.info(f"deleted riddle {riddle_id}")
    return {"msg":"删除成功","id":riddle_id}
    