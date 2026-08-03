import requests

class AIChatBot:
    def __init__(self):
        self.url = "http://localhost:11434/api/chat"
        self.model = "qwen2.5:3b"
        self.messages = []           # 存对话历史
    
    def chat(self, question):
        self.messages.append({"role": "user", "content": question})
        try:
            response = requests.post(self.url, json={
                "model": self.model,
                "messages": self.messages,
                "stream": False
            })
            answer = response.json()["message"]["content"]
            self.messages.append({"role": "assistant", "content": answer})
            return answer
        except Exception as e:
            return f"出错了: {e}"
    
    def run(self):
        print("=== AI 对话助手 ===")
        print("输入 quit 退出\n")
        while True:
            question = input("你: ")
            if question == "quit":
                print("再见！")
                break
            answer = self.chat(question)
            print(f"AI: {answer}\n")

if __name__ == "__main__":
    bot = AIChatBot()
    bot.run()
