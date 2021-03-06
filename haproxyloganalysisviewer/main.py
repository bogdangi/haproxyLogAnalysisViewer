import tornado.ioloop
import tornado.web
import tornado.template
from haproxy.haproxy_logfile import HaproxyLogFile
from haproxy.main import VALID_FILTERS
from haproxy import filters as modFilters
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

class AddFiltersHandler(tornado.web.RequestHandler):
    """Add filters"""
    def get(self):
        filters = [eval('modFilters.filter_' + i) for i in VALID_FILTERS]
        self.render("templates/add-filters.html", log_file=log_file, filters=filters)

    def post(self):
        global log_file
        filters = []
        for filter in self.request.arguments.keys():
            if ''.join(self.request.arguments[filter]):
                filters.append({
                    'name':filter.split('.')[0],
                    'arguments':dict([(i,self.request.arguments[filter]) for i in filter.split('.')[1:]]),
                    }
                    )
        for filter in filters:
            log_file = log_file.filter(
                eval(
                    'modFilters.' + filter['name'] + '(' + ','.join(
                        [i+'="'+''.join(filter['arguments'][i])+'"' for i in filter['arguments'] if ''.join(filter['arguments'][i])]
                        ) + ')'
                    )
                )
        
        filters = [eval('modFilters.filter_' + i) for i in VALID_FILTERS]
        self.render("templates/add-filters.html", log_file=log_file, filters=filters)

class RunCommandHandler(tornado.web.RequestHandler):
    """ Upload files """
    def get(self, command):
        command_string = 'log_file.cmd_{0}()'
        string = 'command: {0}'.format(command)
        result = eval(command_string.format(command))
        self.render("templates/command.html", log_file=log_file, command=command, result=result)

application = tornado.web.Application([
    (r"/", UploadHandler), # Use it as index while create index page
    (r"/upload", UploadHandler),
    (r"/add-filters", AddFiltersHandler),
    (r"/command/(.*)", RunCommandHandler),
    ], debug=True)

def console_script():
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    console_script()
