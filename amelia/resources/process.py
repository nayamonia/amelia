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
import psutil
import settings

class ProcessHandler(main.BaseHandler):
    uri_sufix = "/?([^*]+)"
    
    @web.authenticated
    def get(self, params=False):
        settings.PAGE_TITLE = "Monitor de Processos"
        self.render("process.html", kills=False)
        
        
    def post(self, params=False):
        settings.PAGE_TITLE = "Monitor de Processos"
        pids = self.get_arguments("pid")
        kills = []
        for pid in pids:
            try:
                psutil.Process(int(pid)).kill()
                kills.append({"pid" : pid, "status" : "Finalizado"})
            except Exception, e:
                kills.append({"pid" : pid, "status" : "Erro:%s" % e})
                
        self.render("process.html", kills=kills)
        


            

