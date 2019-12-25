import tornado
import jieba
import json
import tornado.options
import tornado.web
from tornado.options import define, options

# 定义端口为15731
define("port", default=15731, help="run on the given port", type=int)

# 测试
class WordSplitHandler(tornado.web.RequestHandler):
    # get 函数
    def get(self):
        sentence = self.get_argument('sent')
        words = list(jieba.cut(sentence))
        self.write('sent: %s<br>' % sentence)
        self.write('word split: %s<br>' % json.dumps(words, ensure_ascii=False, indent=2))

# 主函数
def server():
    # 开启tornado服务
    tornado.options.parse_command_line()
    # 定义app
    app = tornado.web.Application(
            handlers=[(r'/word_split', WordSplitHandler),
                      ],    # 网页路径控制
          )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

server()

