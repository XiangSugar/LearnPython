# coding = utf-8

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def score_level(score):
    if score > 100:
        raise ValueError('invalid error %s' % score)
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return 'D'


def process_student():
    # 获取当前线程关联的student:
    std   = local_school.student
    score = local_school.score
    level = score_level(score)

    print('Hello, %s (in %s), your score level is %s' % (std, threading.current_thread().name, level))

def process_thread(name, score):
    # 绑定ThreadLocal的student:
    local_school.student = name
    local_school.score   = score
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',70), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',90), name='Thread-B')
t3 = threading.Thread(target= process_thread, args=('Goeiv',110), name = 'Thread-C')
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()