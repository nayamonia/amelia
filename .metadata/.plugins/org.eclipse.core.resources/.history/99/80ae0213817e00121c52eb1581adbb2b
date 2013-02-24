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
from lib.utils import human_size, cmdexec
import datetime
import logging
import platform
import psutil
import socket
import tornado.web

class DashboardModule(tornado.web.UIModule):
    def render(self):
        hostname = socket.gethostname()
        mem = human_size(psutil.TOTAL_PHYMEM, False)
        arch = platform.machine()
        disk =  human_size(psutil.disk_usage("/").total)
#        cpu = cmdexec("dmidecode -t4 | grep Version:")
        cpu = cmdexec('cat /proc/cpuinfo | grep "model name"')
        cpu = cpu[0].split("\n")
        cpu_descr = "%s x %s" % (cpu[0].split(":")[1], psutil.NUM_CPUS)
        
        boot = psutil.BOOT_TIME
        boot = datetime.datetime.fromtimestamp(int(boot)).strftime('%d/%m/%Y %H:%M:%S') 
        
        try:
            manufacturer = cmdexec('dmidecode -t 2 | grep Manufacturer:')
            manufacturer = manufacturer[0].split("\n")
            manufacturer = manufacturer[0].split(":")[1]
        
            product_name = cmdexec('dmidecode -t 2 | grep "Product Name"')
            product_name = product_name[0].split("\n")
            product_name = product_name[0].split(":")[1]
            
            baseboard = manufacturer + " " + product_name
        except Exception, e:
            logging.debug(e)
            baseboard = "Não disponível"
            
        lspci = cmdexec('lspci -m')
        lspci = lspci[0].split('\n')
        pci_list = []
        for pci in lspci:
            pci = pci.split('"')
            try:
                pci_list.append({"type" : pci[1],
                                 "vendor" : pci[3],
                                 "device" : pci[5]})
            except:
                pass
            
        tmplist = sorted(pci_list, key=lambda k: k['type']) 
        pci_list = tmplist
        
        lsusb = cmdexec('lsusb')
        lsusb = lsusb[0].split('\n')
        usb_list = []
        for usb in lsusb:
            usb = usb.split('ID')
            try:
                if not "0000:0000" in usb[1]:
                    usb_list.append({"device" : usb[1]})
            except:
                pass
            
        tmplist = sorted(usb_list, key=lambda k: k['device']) 
        usb_list = tmplist

        try:
            serial_ports = cmdexec('dmesg | grep -i tty | grep "^0"')
            serial_ports = serial_ports[0].split('\n')
            serial_ports = len(serial_ports)
        except:
            serial_ports = "Não disponível"
            
        return self.render_string("modules/dashboard.html", 
                                  hostname=hostname,
                                  mem=mem,
                                  arch=arch,
                                  disk=disk,
                                  cpu=cpu_descr,
                                  boot=boot,
                                  baseboard=baseboard,
                                  pci=pci_list,
                                  usb=usb_list,
                                  serial=serial_ports)
    
    def css_files(self):
        return ["/static/css/content.css", "/static/css/dashboard.css"]    
