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
from lib.utils import saveFile
from tornado import web
import main
import settings

class ConfHandler(main.BaseHandler):
    uri_sufix = "/([^*]+)"
    
    @web.authenticated
    def get(self, params=False):
        settings.PAGE_TITLE = "Configuração"
        self.render("conf.html", params=params, msg=False)
    
    @web.authenticated    
    def post(self, params=False):
        settings.PAGE_TITLE = "Configuração"
        try:
            content_file = self.get_argument("content-file", False)
            if content_file:
                current_file = self.get_argument("current-file", False)
                saveFile(content_file, current_file)
                msg = "Arquivo %s salvo com sucesso!" % current_file
        except Exception, e:
            msg = "Erro ao salvar %s:\n%s" % (current_file, e)

        self.render("conf.html", params=params, msg=msg)

