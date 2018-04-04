# -*- coding :utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)  # 获取文件的大小
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')  # 获取最近一次的修改时间
    flag = '/' if os.path.isdir(f) else ''  # 如果是一个文件夹，则在末尾输出一个 / 的标识符
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))  # 输出格式控制