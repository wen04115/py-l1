import time
import asyncio

async def task1(): #表示task1任务是由事件循环来管理调度，并不是有我们来调度执行
    #time.sleep(5)  # 模拟一个耗时 5 秒的 I/O 操作
    #time.sleep(5)
    #await告诉时间循环此处可挂起，等待await后面的对象执行完毕了在向下执行
    #await后面的对象需要一个使用async def 定义对象
    #time.sleep()需要替换为async def定义版本的sleep函数
    #await time.sleep(5) #同步版本
    await asyncio.sleep(5) #异步版本
    return 10

async def task2():
    #time.sleep(3)  # 模拟一个耗时 3 秒的 I/O 操作
    await asyncio.sleep(3)
    return 20

async def main():
    #获取事件循环
    #手动注册任务
    result=await asyncio.gather(task1(),task2())   #一行代码同时完成两个任务的事件循环和注册
    print(result)

if __name__ == '__main__':
    start = time.time()
    #创建事件循环
    #启动事件循环
    asyncio.run(main()) #一行代码就能同时完成创建和启动
    print('总耗时:', time.time() - start)
