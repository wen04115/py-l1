import asyncio
import httpx

class AIChatBot:
    def __init__(self):
        self.url = "http://localhost:11434/api/chat"
        self.model = "qwen2.5:3b"
        self.message = []  #存历史对话

    async def chat(self,question):
        self.message.append({"role": "user", "content": question})
        try:
            async with httpx.AsyncClient() as client:
                response =await client.post(self.url,json={
                    "model": self.model,
                    "messages": self.message,
                    "stream": False
                })    
            answer =response.json()["message"]["content"]
            self.message.append({"role": "assistant", "content": answer})
            return answer
        except Exception as e:
            raise
    async def run(self):
        print("=== AI 对话助手（异步版）===")
        print("输入 quit 退出\n")
        while True:
            question = input("你:")
            if question == "quit":
                print("再见！")
                break
            answer =await self.chat(question)
            print(f"AI: {answer}\n")

if __name__ == "__main__":
    bot=AIChatBot()
    asyncio.run(bot.run())                             