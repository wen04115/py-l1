from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "你是{role}，回答要{style}。"),
    ("user", "{question}")
])
llm = ChatOllama(model="qwen2.5:3b")
chain = prompt | llm
resp = chain.invoke({"role": "Python老师", "style": "简洁+带一个例子", "question": "啥是装饰器"})
print(resp.content)
