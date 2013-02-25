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
from lib.utils import getFilenamePath
from ui_modules.conf import ConfModule
from ui_modules.content import ContentModule
from ui_modules.dashboard import DashboardModule
from ui_modules.left import LeftModule
from ui_modules.menuitem import MenuItemModule
from ui_modules.navigate import NavigateModule
#from ui_modules.packages import PackagesModule
from ui_modules.process import ProcessModule
from ui_modules.top import TopModule
import logging
import os
import socket

VERSION = "1.4"

IP = socket.gethostbyname(socket.gethostname())
HOSTNAME = socket.gethostname()

PAGE_TITLE = HOSTNAME

HTTP_SERVER_IP = socket.gethostbyname(socket.gethostname())
HTTP_PORTA_PADRAO = 8080
HTTP_URI_HOME = "http://%s:%s" % (HTTP_SERVER_IP, 
                                  HTTP_PORTA_PADRAO)
HTTP_STATIC_PATH = {"path": "static"}
HTTP_REPO_PATH = {"path": HTTP_STATIC_PATH["path"],
                  "uri": ("%s/static" % HTTP_URI_HOME)}

MENU= [{"DESCRIPTION" : "Início", "URI" : "/", "IMG" : "mycomp32.png"}, 
       {"DESCRIPTION" : "Display", "URI" : "/novnc/?true_color=0", "IMG" : "display32.png"}, 
       {"DESCRIPTION" : "Processos", "URI" : "/process" , "IMG" : "task32.png"}, 
       {"DESCRIPTION" : "Configurar", "URI" : "/conf", "IMG" : "conf32.png"}, 
#       {"DESCRIPTION" : "Pacotes", "URI" : "/software", "IMG" : "pkg32.png"}, 
       {"DESCRIPTION" : "Terminal", "URI" : "/console", "IMG" : "terminal32.png"}, 
       {"DESCRIPTION" : "Jobs", "URI" : "/job", "IMG" : "jobs32.png"}, 
       {"DESCRIPTION" : "Logs", "URI" : "/log", "IMG" : "log32.png"},] 

UI_MODULES = {
              "Left" : LeftModule, 
              "Top" : TopModule,
              "MenuItem" : MenuItemModule,
              "Navigate" : NavigateModule,  
              "Content" : ContentModule,
              "Dashboard" : DashboardModule,
              "Process" : ProcessModule,
#              "Packages": PackagesModule,
              "Conf": ConfModule,
             }

SETTINGS = dict(
                template_path = os.path.join(os.path.dirname(__file__), 
                                             "templates"),
                static_path = os.path.join(os.path.dirname(__file__), 
                                           "static"),
                site_title = "APOS %s" % VERSION, 
                login_url = "/login",
                cookie_secret = "77XvAF5TTj2TxQ5ZAU+p4HYuYyoIf0EIuuo6cKCHKnQ=",
                autoescape = None,
                ui_modules = UI_MODULES,
                debug = True,
                uri_home = HTTP_URI_HOME, 
               )

LOGFILE = getFilenamePath('/tmp/apos.log')          
logging.basicConfig(
                    level = logging.DEBUG,
                    format = '%(asctime)s : %(levelname)s : %(message)s',
                    filename = LOGFILE,
                    filemode = 'a',
                   )
