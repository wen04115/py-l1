# AI 汉字谜盒

FastAPI + Ollama 全栈猜字谜应用

## 技术栈
- 后端：FastAPI + requests + JSON 文件存储
- 前端：HTML + CSS + 原生 JS
- AI：Ollama 本地模型（qwen2.5:3b）

## 接口
| 方法 | 路径 | 说明 |
|---|---|---|
| GET | / | 首页 |
| POST | /api/sessions | 新建会话 |
| GET | /api/sessions | 会话列表 |
| POST | /api/chat | 与 AI 对话 |
| GET | /api/sessions/{id} | 加载会话 |
| DELETE | /api/sessions/{id} | 删除会话 |

## 启动
1. 启动 Ollama（模型 qwen2.5:3b）
2. pip install fastapi uvicorn requests
3. python 02.汉字谜盒案例.py
4. 打开 http://127.0.0.1:8000
