# py-l1

Python 学习代码 + AI 应用项目。

## 项目

### AI 对话助手（ai_chat.py）

基于 Ollama 本地大模型的对话机器人，支持多轮对话记忆。

- **OOP 结构**：AIChatBot 类（__init__ / chat / run）
- **多轮记忆**：messages 列表保存对话历史，AI 能回忆之前的内容
- **异常处理**：Ollama 未运行时不会崩溃
- **模型**：qwen2.5:3b（本地运行，不联网不花钱）

运行：
```bash
# 1. 启动 Ollama（托盘有图标即可）
# 2. 确认模型已下载
ollama list   # 应该看到 qwen2.5:3b

# 3. 运行程序
python ai_chat.py
```

### 汉字谜盒 API（first_api.py + React 前端）

基于 FastAPI 的汉字谜语管理后端（全栈项目 1），配套 React 前端 hanzi-box，带日志和自动化测试。

- **增删查接口**：GET/POST /api/riddles、GET/DELETE /api/riddles/{id}
- **JSON 持久化**：riddle.json 存数据，启动自动加载
- **logging 日志**：分级（INFO/WARNING/DEBUG），双写终端 + riddle_api.log 文件
- **pytest 测试**：4 个接口测试全过（test_api.py）

运行：
```bash
uvicorn first_api:app --reload --port 8000   # 启动后端（py-l1 目录）
pytest test_api.py -v                        # 跑测试，4 passed
```



## 技术栈

- Python 3.12.7
- requests（HTTP 请求）
- Ollama + qwen2.5:3b（本地 LLM）
- Cursor IDE
- Git + GitHub
- FastAPI + uvicorn（Web API 后端）
- pytest + httpx（接口自动化测试）
- React + Vite + axios（前端 hanzi-box）
