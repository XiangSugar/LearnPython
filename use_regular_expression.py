# coding : utf-8

import re


test = '010-123456'
if re.match(r'^\d{3}\-\d{3,8}$', test):
    print('OK!')
else:
    print('Failed!')

print(re.split(r'[\s\,]+', 'a, b,c,  d'))

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-456782')
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 编译
# 编译后生成 regular expression 对象，此对象中已经包含了正则表达式
# 所以调用对应的方法时不用再给出正则字符串
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
print(re_telephone.match('028-87966745').groups())