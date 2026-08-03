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

### Python 基础练习

| 文件 | 内容 |
|------|------|
| 01.第一章/moxie.py | 默写练习 |
| 02.第二章/成绩判定程序.py | match-case |
| 02.第二章/猜数字游戏.py | while + random |
| 03.第三章/代办事项管理器.py | 列表操作 |
| 03.第三章/购物车管理系统.py | 字典操作 |
| 03.第三章/通讯录管理系统.py | 嵌套字典 |
| 04.第四章/ | OOP 面向对象 |

## 技术栈

- Python 3.12.7
- requests（HTTP 请求）
- Ollama + qwen2.5:3b（本地 LLM）
- Cursor IDE
- Git + GitHub
