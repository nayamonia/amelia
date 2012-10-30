# encoding: utf-8
"""
The MIT License (MIT)

Copyright (c) 2012 Gabriel Fernandes

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to 
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER 
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN 
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from lib.utils import getResources
from tornado import httpserver, ioloop, web
from tornado.options import define, options
from tornado.util import import_object
import tornado.options
import logging
import settings
import threading
import time

def Start(port):
    try:
        settings.HTTP_PORTA_PADRAO = port
        application = AmeliaApplication()
        http_server = httpserver.HTTPServer(application)
        http_server.listen(port)
        ioloop.IOLoop.instance().start()
        logging.info("Amelia server started")
        
    except Exception, e:
        logging.error("error starting Amelia server:\n%s", e)


class AmeliaApplication(web.Application):
    listaURIs = []

    def __init__(self):        
        web.Application.__init__(self, 
                                 AmeliaApplication.RefreshHandlers(self), 
                                 **settings.SETTINGS)
        
    def RefreshHandlers(self):
        path = __file__
        path = path[:-7]
        handlers = []
        for item in getResources(path):
            try:
                handler = import_object("resources.%s.%sHandler" 
                                        % (item, item.capitalize()))
                handlers.append((r"/%s" % (item), handler))
                self.listaURIs.append((r"/%s" % (item)))
                try:
                    handlers.append((r"/%s%s" % (item, 
                                                 handler.uri_sufix),
                                                 handler))
                except:
                    pass
            except:
                logging.error("error create uri resources.%s.%sHandler" 
                              % (item, item.capitalize()))
        handlers.append((r"/", HomeHandler))
        handlers.append((r"/static/(.*)" , 
                         web.StaticFileHandler, settings.HTTP_STATIC_PATH))
        return handlers
    
class BaseHandler(web.RequestHandler):
    SUPPORTED_METHODS = ("GET", "HEAD", "POST", "DELETE", "PUT")
    _list_thread_kill = []
    
    def get_current_user(self):
        return self.get_secure_cookie("username")

    def HTTPError(self, code, message):
        logging.info(message)
        raise web.HTTPError(code)

    def get_thread_history(self):
        return self._list_thread_kill
    
    def add_thread_history(self, thread, location):
        self._list_thread_kill.append(dict(
                                           NAME=thread.name, 
                                           IDENT=thread.ident, 
                                           SINCE=thread.since,
                                           FINISH=time.strftime("%Y-%m-%d %H:%M:%S"),
                                           LOCATION=location,
                                           TIMESTAMP=thread.timestamp,
                                           URI=str(thread.ident) + "/" + \
                                               str(thread.timestamp), 
                                           )
                                      )
    
    def get_thread_list(self):
        """
        Retorna a list de threads vivas
        """
        list_thread = [] 
        main_thread = threading.currentThread()
        for thread in threading.enumerate():
            if thread is main_thread:
                continue
            try:
                list_thread.append(dict(
                                        NAME=thread.name, 
                                        IDENT=thread.ident, 
                                        SINCE=thread.since,
                                        TIMESTAMP=thread.timestamp,
                                        URI=str(thread.ident) + "/" + \
                                            str(thread.timestamp), 
                                        )
                                   )
            except:
                pass
            
        return list_thread       
    
    def get_thread(self, thread_ident, timestamp):
        """Retorna a thread identificado por thread_ident
        """
        main_thread = threading.currentThread()
        for thread in threading.enumerate():
            if thread is main_thread:
                continue
            if thread.ident == int(thread_ident) and \
               str(thread.timestamp) == str(timestamp):
                return thread       

    def get_thread_ended(self, thread_ident, timestamp):
        """Retorna info da thread encerrada identificada por thread_ident
        """
        list_thread = self.get_thread_history()
        if list_thread:
            for thread in list_thread:
                if str(thread["IDENT"]) == str(thread_ident) and \
                   str(thread["TIMESTAMP"]) == str(timestamp):
                    return thread 
    
    def thread_ident(self, thread_name):
        """Retorna um inteiro com o identificador da thread ou nada
        """
        main_thread = threading.currentThread()
        for thread in threading.enumerate():
            if thread is main_thread:
                continue
            if thread.getName() == thread_name:
                return thread.ident, thread.timestamp       
        
class HomeHandler(BaseHandler):
    @web.authenticated
    def get(self):       
        settings.PAGE_TITLE = "Início" 
        self.render("index.html")

if __name__ == "__main__":
    define("port", default=8080, help="port will run server", type=int)
    tornado.options.parse_command_line()
    Start(options.port)
