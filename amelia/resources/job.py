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
from tornado import web
import main
import settings
import threading

class JobHandler(main.BaseHandler):
    uri_sufix = "/([^*]+)"

    def get(self, params=""):
        settings.PAGE_TITLE = "Jobs"
        if params != "":
            self.params = params.split('/')
            if len(self.params) == 2:
                ident = self.params[0]
                timestamp = self.params[1]
                thread = self.get_thread(ident, timestamp)
                if isinstance(thread, threading.Thread):
                    status = str(thread.status)
                else:
                    thread = self.get_thread_ended(ident, timestamp)
                    if thread:
                        status = str(thread)
                    else:
                        status = "Job unavailable"
            self.render("job.html", status=status)
                
        else:
            self.render("job.html", status=False,
                        jobs_alive=self.get_thread_list(), 
                        jobs_ended=self.get_thread_history())
#            list_thread_alive = self.get_thread_list()
#            list_thread_ended = self.get_thread_history()
#            thread_status = dict(ALIVE=list_thread_alive,
#                                 ENDED=list_thread_ended)
#            self.render("job.html", 
#                        jobs_alive=list_thread_alive, 
#                        jobs_ended=list_thread_ended,
#                        status=False)
