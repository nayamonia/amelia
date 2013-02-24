# encoding: utf-8
#verificar codigo nao usado
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
import datetime
import json
import logging
import os
import platform
import time
import subprocess

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

def human_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

def cmdexec(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                         shell=True)
    out, error = p.communicate()
    return out, error

def getFileList(path, ext):
    file_list = []
    files = os.listdir(os.path.dirname(path))
    for item in files:
        if (".%s" % ext).upper() in item.upper() and \
            not item.startswith("__") and \
            not item.startswith("."):
            file_list.append(item)
    return tuple(file_list)

def getResources(path):
    listaResources = []
    resources = os.listdir(os.path.join(os.path.dirname(path), "resources"))
    for item in resources:
        if ".pyc" not in item and \
            not item.startswith("__") and \
            not item.startswith("."):
             
            item = item.replace(".py","")
            listaResources.append(item)
    return tuple(listaResources)

def json2list_dict(body):
    json_body = json.loads(json.dumps())
    if not isinstance (json_body, list):
        json_body = [json_body]
    return json_body
    
def getFilenamePath(filename):
    
    try:
        if platform.platform().startswith('Windows'):
            log_file = os.path.join(os.getenv('HOMEDRIVE'), 
                                       os.getenv('HOMEPATH'), filename)
        else:
            log_file = os.path.join(os.getenv('HOME'), filename)
            
        return log_file
    except:
        return filename
        
def saveFile(lines, filename):
    try:
        f = open(filename, 'w')
        f.writelines(lines)
        logging.info("created " + f.name)
    except Exception, e:
        logging.error("error on create %s:\n%s" % (f.name, e))                
    finally:
        f.close()
    return f.name

def getMySQLDate(date):
    date = datetime.datetime.fromtimestamp(time.mktime(\
                                           time.strptime(date, '%d%m%Y')))
    return date.strftime('%Y-%m-%d') 
        
def timedelta2str(timedelta):
    sec = timedelta.days * 24 * 60 * 60 + timedelta.seconds
    min, sec = divmod(sec, 60)
    hrs, min = divmod(min, 60)
    return '%02d:%02d:%02d' % (hrs, min, sec)  

def mod11(list, max_weight=9):
    sum = 0
    weight = 2
    
    for item in reversed(list):
        sum += int(item) * weight
        weight += 1
        if weight > max_weight:
            weight = 2
    
    mod = 11 - sum % 11
    if mod > 9:
        return 0
    else:
        return mod
    
        
