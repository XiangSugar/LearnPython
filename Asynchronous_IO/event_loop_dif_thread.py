# coding = utf-8

from threading import Thread, currentThread
import asyncio
import time

now = lambda: time.time()

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
 
def more_work(x):
    print('%s' % currentThread())
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))

start = now()
new_loop = asyncio.new_event_loop()
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print('TIME: {}'.format(time.time() - start))
print('%s' % currentThread())
 
new_loop.call_soon_threadsafe(more_work, 6)
new_loop.call_soon_threadsafe(more_work, 3)

# '''
# 启动上述代码之后，当前线程不会被 block，新线程中会按照顺序执行
#  call_soon_threadsafe 方法注册的 more_work 方法，后者因为 
#  time.sleep 操作是同步阻塞的，因此运行完毕 more_work 需要大致 6 + 3
# '''