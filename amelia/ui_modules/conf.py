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
from profiles.profile import PROFILES
import tornado.web

class ConfModule(tornado.web.UIModule):
    def render(self, params=False):
        profile_list = False 
        current_profile = False
        file_list = False
        current_file = False
        content_file = False
               
        if not params:
            profile_list = []
            for PROFILE in PROFILES:
                profile_list.append(PROFILE["HEADER"])
        else:
            self.params = params.split("/")
            if len(self.params) == 1:
                for PROFILE in PROFILES:
                    if PROFILE["HEADER"]["name"] == self.params[0]:
                        file_list = PROFILE["CONFIG_FILES"]
                        current_profile = self.params[0]
                        break 
            else:
                for PROFILE in PROFILES:
                    if PROFILE["HEADER"]["name"] == self.params[0]:
                        current_profile = self.params[0]
                        file_list = PROFILE["CONFIG_FILES"]
                        for file in file_list:
                            if file["name"] == self.params[1]:
                                current_file = file
                                f = open("%s/%s" % (current_file["path"], current_file["name"]),
                                         'r')
                                lines = f.readlines()
                                f.close()
                                content_file = ""
                                for line in lines:
                                    content_file += line
                                break
                    
        return self.render_string("modules/conf.html", 
                                  profile_list=profile_list,
                                  file_list=file_list,
                                  current_profile=current_profile,
                                  current_file=current_file,
                                  content_file=content_file,
                                  msg="")
    
    def css_files(self):
        return ["/static/css/content.css", "/static/css/conf.css"]    

