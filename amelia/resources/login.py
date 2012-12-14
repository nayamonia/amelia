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
import main
import settings
import tornado
import PAM

class LoginHandler(main.BaseHandler):
    def get(self):
        settings.PAGE_TITLE = "Login"
        self.render("login.html", 
                    next=tornado.escape.url_escape(self.get_argument("next","")))        
    def post(self):
        settings.PAGE_TITLE = "Login"
        if self.is_authorized(self.get_argument("username"),self.get_argument("password")):
            self.set_secure_cookie("username", self.get_argument("username"), 1)
            self.redirect(self.get_argument("next", "/"))
        else:
            """ Fix this code and show the error message... """
            self.redirect(self.get_argument("next", "/?err=InvalidUser"))
        

    def is_authorized(self, username, password):
        """
        Returns true is a user is authorised via PAM.
    
        Note: We use the 'login' PAM stack rather than inventing our own.
        """
        pam_auth = PAM.pam()
    
        pam_auth.start('login')
        pam_auth.set_item(PAM.PAM_USER, username)
        pam_auth.set_item(PAM.PAM_TTY, 'console')
    
        def _pam_conv(auth, query_list, user_data=None):
            resp = []
            for i in range(len(query_list)):
                query, qtype = query_list[i]
                if qtype == PAM.PAM_PROMPT_ECHO_ON:
                    resp.append((username, 0))
                elif qtype == PAM.PAM_PROMPT_ECHO_OFF:
                    resp.append((password, 0))
                else:
                    return None
            return resp
    
        pam_auth.set_item(PAM.PAM_CONV, _pam_conv)
    
        try:
            pam_auth.authenticate()
            pam_auth.acct_mgmt()
        except Exception, e:
            print 'Error with PAM: %s' % e
            return False
        else:
            return True