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
    event_loop = asyncio.get_running_loop()
    #手动注册任务
    t1 = event_loop.create_task(task1())
    t2 = event_loop.create_task(task2())
    #等待t1任务执行结果，并且获取t1任务的执行结果
    result = await task1()
    print('任务1执行结果:', result)
    #等待t2任务执行结果，并且获取t2任务的执行结果
    result = await task2()
    print('任务2执行结果:', result)

if __name__ == '__main__':
    start = time.time()  #time.time() = 模块名.函数名 () time：导入的 Python 内置时间模块   time()：time 模块内部自带的获取时间戳的函数
   #创建事件循环
    event_loop = asyncio.get_event_loop()
    #启动事件循环
    event_loop.run_until_complete(main()) #  main()是事件循环的入口 调用上面的main 方法 可以换名字 不过一般定义的都是main
    
    print('总耗时:', time.time() - start)
