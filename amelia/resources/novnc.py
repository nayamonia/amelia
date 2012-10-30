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

class NovncHandler(main.BaseHandler):
    uri_sufix = "/?([^*]+)"
    
    @web.authenticated
    def get(self, params=False):
        settings.PAGE_TITLE = "Display"
        
        noVNC = """
            <script>
            /*jslint white: false */
            /*global window, $, Util, RFB, */
            "use strict";
    
            var rfb;
    
            function getPassword(rfb) {
                var msg;
                msg = '<form onsubmit="return setPassword();"';
                msg += '  style="margin-bottom: 0px">';
                msg += 'Digite a senha: ';
                msg += '<input type=password size=10 id="password_input" class="status">';
                msg += '<\/form>';
                $D('status_bar').setAttribute("class", "status_warn");
                $D('status').innerHTML = msg;
            }
            function setPassword() {
                rfb.sendPassword($D('password_input').value);
                return false;
            }
            function updateState(rfb, state, oldstate, msg) {
                var s, sb, level;
                s = $D('status');
                sb = $D('status_bar');
                switch (state) {
                    case 'failed':       level = "error";  break;
                    case 'fatal':        level = "error";  break;
                    case 'normal':       level = "normal"; break;
                    case 'disconnected': level = "normal"; break;
                    case 'loaded':       level = "normal"; break;
                    default:             level = "warn";   break;
                }
    
                if (typeof(msg) !== 'undefined') {
                    sb.setAttribute("class", "status_" + level);
                    s.innerHTML = msg;
                }
            }
    
            window.onload = function () {
                var host, port, password, path, token;
    
                host = '%s';
                port = '6080';
                password = WebUtil.getQueryVar('password', '');
                path = WebUtil.getQueryVar('path', 'websockify');
    
                rfb = new RFB({'target':       $D('canvas'),
                               'encrypt':      0,
                               'repeaterID':   '',
                               'true_color':   WebUtil.getQueryVar('true_color', true),
                               'local_cursor': WebUtil.getQueryVar('cursor', true),
                               'shared':       WebUtil.getQueryVar('shared', true),
                               'view_only':    WebUtil.getQueryVar('view_only', false),
                               'updateState':  updateState,
                               'onPasswordRequired':  getPassword});
                rfb.connect(host, port, password, path);
            };
            </script>
        
        """ % settings.HTTP_SERVER_IP
        
        self.render("novnc.html", noVNC=noVNC)
        
        
    


            

