import time

def task1():
    time.sleep(5)  # 模拟一个耗时 5 秒的 I/O 操作
    return 10

def task2():
    time.sleep(3)  # 模拟一个耗时 3 秒的 I/O 操作
    return 20

def main():
    result = task1()
    print('任务1执行结果:', result)
    result = task2()
    print('任务2执行结果:', result)

if __name__ == '__main__':
    #在运行`main()函数之前，先记下此刻的时间，存进变量start，当作计时起点
    start = time.time()  #time.time() = 模块名.函数名 () time：导入的 Python 内置时间模块   time()：time 模块内部自带的获取时间戳的函数
    #获取当前系统时间戳 time.time()
    main()  #运行包含 task1、task2 的主程序（串行执行睡眠 5 秒 + 3 秒）
    print('总耗时:', time.time() - start)
