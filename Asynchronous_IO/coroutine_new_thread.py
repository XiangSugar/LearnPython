# coding = utf-8

from threading import Thread, currentThread
import asyncio
import time

now = lambda: time.time()

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()
 
async def do_some_work(x):
    print('%s' % currentThread())
    print('Waiting {}'.format(x))
    await asyncio.sleep(x)
    print('Done after {}s'.format(x))
 
def more_work(x):
    print('More work {}'.format(x))
    time.sleep(x)
    print('Finished more work {}'.format(x))
 
start    = now()
new_loop = asyncio.new_event_loop()
t        = Thread(target=start_loop, args=(new_loop,))
t.start()
print('%s' % currentThread())
 
resul1 = asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
resul2 = asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)
print('Task ret: ', resul1.result())
print('Task ret: ', resul2.result())
print('TIME: {}'.format(time.time() - start))

