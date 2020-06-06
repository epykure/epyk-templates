import os

import tornado.ioloop
import tornado.web


cur_dir = os.path.dirname(os.path.abspath(__file__))


class MainHandler(tornado.web.RequestHandler):
    def get(self):
      self.render_string(os.path.join(cur_dir, "front_end", "rest_bb_post.html"))


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
