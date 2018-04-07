# -*- coding :utf-8 -*-
# about multiprocessing

from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')

# 在调试台中运行，得到的结果和网站上面给出的不一样
# 不过在 cmd 终端上运行 .py 文件，则能够得到一致的结果