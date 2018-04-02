# -*- coding : utf-8 -*-
# How to use python to write file

# 'w' 会覆盖文件（如果文件存在，会先删除然后重新写一个文件）
with open('/Users/Sxiang/Documents/write_test.txt', 'w') as f1:
    f1.write('Hello, world!')

# 'a' 追加模式（如果文件存在，则写入的内容只是添加在原有文件的后面）
with open('/Users/Sxiang/Documents/write_test.txt', 'w', 'a') as f2:
    f2.write('Hello, world!')

# 制定编码
with open('/Users/Sxiang/Documents/write_test.txt', 'w', encoding = 'utf-8') as f3:
    f3.write('Hello, world!')