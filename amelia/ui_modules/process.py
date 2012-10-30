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
from lib.utils import human_size
import psutil
import tornado.web

class ProcessModule(tornado.web.UIModule):
    def render(self, kills=False):
        ps_list = []
        for ps in psutil.process_iter():
            ps_list.append({"name" : ps.name,
                            "username" : ps.username,
                            "cpu" : "%0.2f" % ps.get_cpu_percent(interval=0),
                            "pid" : ps.pid,
                            "memory" : human_size(ps.get_memory_info().rss,
                                                  True)})
            ps_list.sort(reverse=True)
            
        return self.render_string("modules/process.html", 
                                  ps_list=ps_list, kills=kills)
    
    def css_files(self):
        return ["/static/css/content.css", "/static/css/process.css"]    

    def embedded_javascript(self):
        return """
                var i=30;
                var pause=false;
                function count() {
                    if (!pause) {
                        document.getElementById('time').innerHTML=i;
                        if (i==0) {
                            document.location.reload();
                        } else {
                            i=i-1;
                            setTimeout("count()", 1000);
                        }
                    }
                }
                count();
               """


