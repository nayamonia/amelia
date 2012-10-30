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
import logging
import main
import settings

class LogHandler(main.BaseHandler):
    @web.authenticated
    def get(self):
        settings.PAGE_TITLE = "Logs"
        f = open(settings.LOGFILE)
        linhas = f.readlines()
        logging.info("Exibindo log " + f.name)
        i = 0
        saida = "<textarea class='field-text padlog' rows='50' readonly>"
        linhas.reverse()
        for linha in linhas:
            saida += linha
            i += 1
            if i == 500:
                break
        saida += "</textarea>"
        settings.PAGE_TITLE = "Log"
        self.render("log.html", log=saida)


            

