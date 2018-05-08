# -*- coding:utf-8 -*-

# 导入该演示用例代码中必须的 tornado 的四个模块
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

# 用于从命令行中读取配置和解析命令
# 定义一个配置选项port，即端口
# defualt 表示默认值， help表示在帮助中显示的信息 
# type 表示该配置参数的数据类型，如果类型匹配错误会报错
define("port", default=8000, help="run on the given port", type=int)

# 页面请求的Handler类，继承了Web的RequestHandler类
# 此处只有一个get方法，表示Http的Get请求
# 内建方法get_argument用来获取http页面的请求参数
# 内建方法write，将响应的内容写道页面中
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', tornado!')

if __name__ == "__main__":
    # 从命令行中读取并解析配置参数
    tornado.options.parse_command_line()
    # 创建一个tornado应用。handlers 是一个元组列表，其中每个元组的第一个元素是一个正则表达式，
    # 表示网址路由，如果其中包含捕获分组，则将匹配的内容送往 RequestHandler；
    # 第二个元素是所使用的 RequestHandler 类用来响应操作
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    # 使用这个tornado 应用创建一个http服务器
    http_server = tornado.httpserver.HTTPServer(app)
    # 设置 http 服务器的监听端口，命令行有传入端口则监听传入端口，没有则监听默认端口
    http_server.listen(options.port)
    # 启动服务器
    tornado.ioloop.IOLoop.instance().start()