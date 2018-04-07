# -*- coding : utf-8 -*-
# 用进程池的方式大量创建进程

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    # 延时一小段时间  模拟任务执行所花去的时间
    time.sleep(random.random() * 3)
    end = time.time()
    # 打印进程执行所用的时间
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())

    # 最多同时执行几个进程
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))  # 这里是一个 tuple 
    print('Waiting for all subprocesses done...')

    p.close()
    # Pool 对象调用 join() 方法会等待所有子进程执行完毕
    # 调用 join() 之前要先调用 close()
    # 调用 close() 之后就不能继续添加 Process 了
    p.join()
    print('All subprocesses done.')

# -----------命令行中运行结果-----------
# Parent process 9036.
# Waiting for all subprocesses done...
# Run task 0 (8552)...
# Run task 1 (7372)...
# Run task 2 (26648)...
# Run task 3 (10112)...
# Task 2 runs 0.84 seconds.
# Run task 4 (26648)...
# Task 3 runs 0.87 seconds.
# Task 1 runs 1.01 seconds.
# Task 4 runs 0.86 seconds.
# Task 0 runs 2.37 seconds.
# All subprocesses done.