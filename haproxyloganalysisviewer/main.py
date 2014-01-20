import tornado.ioloop
import tornado.web
import tornado.template
from haproxy.haproxy_logfile import HaproxyLogFile
import StringIO

log_file = HaproxyLogFile()

class UploadHandler(tornado.web.RequestHandler):
    """ Upload files """
    def get(self):
        self.render("templates/upload.html", log_file=log_file)

    def post(self):
        global log_file
        if hasattr(self.request,'files'):
            log_file_data = StringIO.StringIO(self.request.files.get('logfile')[0]['body'])
            if log_file_data is not None:
                log_file.parse_data(log_file_data)
        self.render("templates/upload.html", log_file=log_file)

class RunCommandHandler(tornado.web.RequestHandler):
    """ Upload files """
    def get(self, command):
        command_string = 'log_file.cmd_{0}()'
        string = 'command: {0}'.format(command)
        result = eval(command_string.format(command))
        self.render("templates/command.html", log_file=log_file, command=command, result=result)

application = tornado.web.Application([
    (r"/upload", UploadHandler),
    (r"/command/(.*)", RunCommandHandler),
    ], debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
