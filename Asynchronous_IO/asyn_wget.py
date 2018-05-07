# coding = utf-8
# asyn_wget.py


import asyncio

# @asyncio.coroutine
async def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    await writer.drain()
    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# -------------------------------------------------------------------------------------------
# wget www.sohu.com...
# wget www.163.com...
# wget www.sina.com.cn...
# www.163.com header > HTTP/1.0 302 Moved Temporarily
# www.163.com header > Server: Cdn Cache Server V2.0
# www.163.com header > Date: Mon, 07 May 2018 07:29:45 GMT
# www.163.com header > Content-Length: 0
# www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
# www.163.com header > Connection: close
# www.sina.com.cn header > HTTP/1.1 200 OK
# www.sina.com.cn header > Server: Tengine
# www.sina.com.cn header > Content-Type: text/html
# www.sina.com.cn header > Content-Length: 587655
# www.sina.com.cn header > Connection: close
# www.sina.com.cn header > Date: Mon, 07 May 2018 07:28:48 GMT
# www.sina.com.cn header > Expires: Mon, 07 May 2018 07:29:48 GMT
# www.sina.com.cn header > Cache-Control: max-age=60
# www.sina.com.cn header > Vary: Accept-Encoding
# www.sina.com.cn header > Via: http/1.1 cmcc.guangzhou.ha2ts4.136 (ApacheTrafficServer/6.2.1 [cHs f ]), cache20.l2nu20-3[0,304-0,H], cache6.l2nu20-3[1,0], cache6.cn60[0,200-0,H], cache4.cn60[1,0]
# www.sina.com.cn header > X-Via-CDN: f=alicdn,s=cache4.cn60,c=211.67.20.127;f=edge,s=cmcc.guangzhou.ha2ts4.136.nb.sinaedge.com,c=120.221.83.155;f=Edge,s=cmcc.guangzhou.ha2ts4.136,c=183.232.24.136
# www.sina.com.cn header > X-Via-Edge: 15256781283559b53dd78de18e8b739b60c2d
# www.sina.com.cn header > Last-Modified: Mon, 07 May 2018 07:26:25 GMT
# www.sina.com.cn header > X-Powered-By: shci_v1.03
# www.sina.com.cn header > Age: 57
# www.sina.com.cn header > X-Cache: HIT TCP_MEM_HIT dirn:-2:-2 mlen:-1
# www.sina.com.cn header > X-Swift-SaveTime: Mon, 07 May 2018 07:29:04 GMT
# www.sina.com.cn header > X-Swift-CacheTime: 44
# www.sina.com.cn header > Timing-Allow-Origin: *
# www.sina.com.cn header > EagleId: 3acdddcc15256781854513691e
# www.sohu.com header > HTTP/1.1 200 OK
# www.sohu.com header > Content-Type: text/html;charset=UTF-8
# www.sohu.com header > Connection: close
# www.sohu.com header > Server: nginx
# www.sohu.com header > Date: Mon, 07 May 2018 07:29:18 GMT
# www.sohu.com header > Cache-Control: max-age=60
# www.sohu.com header > X-From-Sohu: X-SRC-Cached
# www.sohu.com header > Content-Encoding: gzip
# www.sohu.com header > FSS-Cache: HIT from 8162289.14912507.8916056
# www.sohu.com header > FSS-Proxy: Powered by 2853792.4295594.3607478
# -------------------------------------------------------------------------------------------