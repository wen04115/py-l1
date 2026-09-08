from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

llm = ChatOllama(model="qwen2.5:3b")
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个helpful的助手，回答简洁+带一个例子。"),
    MessagesPlaceholder("history"), # ← 这就是 Memory插槽
    ("human", "{input}")
])
chain = prompt | llm

history = []  # 记忆列表，每轮累加
print("AI: 你好，我是你的本地助手（输入 quit退出）")
while True:
    user_input = input("你: ")
    if user_input.lower() in ("quit", "exit"): break
    resp = chain.invoke({"history": history, "input": user_input})
    print("AI:", resp.content)
    # 这轮的"你说"和"AI回"塞进 history → 下轮自动带上去
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=resp.content))
print("AI: 88，下次再聊~")
