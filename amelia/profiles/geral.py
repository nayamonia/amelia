#!/usr/bin/env python
# encoding: utf-8
from lib.utils import getIFileList

# Configs para Geral
# Arquivos de configuração

HEADER = {"name" : "Sistema",
          "description" : "Configurações do sistema operacional e ferramentas",
          "icon" : "computer.png",}

CONFIG_FILES = []

dir_list, file_list = getIFileList("/usr/local/bin/")
for filename, mime_type in file_list:
    dict_file = {"name" : filename, 
                 "path" : "/usr/local/bin/",
                 "summary" : mime_type,
                 "description" : """
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                        sunt in culpa qui officia deserunt mollit anim id est laborum.
                 """,}    
    CONFIG_FILES.append(dict_file)

dir_list, file_list = getIFileList("/etc/")
for filename, mime_type in file_list:
    if "amelia" in filename:
        dict_file = {"name" : filename, 
                     "path" : "/etc/",
                     "summary" : mime_type,
                     "description" : """
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                            sunt in culpa qui officia deserunt mollit anim id est laborum.
                     """,}    
        CONFIG_FILES.append(dict_file)

dir_list, file_list = getIFileList("/etc/yum.repos.d/")
for filename, mime_type in file_list:
    dict_file = {"name" : filename, 
                 "path" : "/etc/yum.repos.d/",
                 "summary" : mime_type,
                 "description" : """
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                        sunt in culpa qui officia deserunt mollit anim id est laborum.
                 """,}    
    CONFIG_FILES.append(dict_file)

dir_list, file_list = getIFileList("/etc/ld.so.conf.d/")
for filename, mime_type in file_list:
    dict_file = {"name" : filename, 
                 "path" : "/etc/ld.so.conf.d/",
                 "summary" : mime_type,
                 "description" : """
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                        sunt in culpa qui officia deserunt mollit anim id est laborum.
                 """,}    
    CONFIG_FILES.append(dict_file)

dict_file = {"name" : "rc.local", 
             "path" : "/etc/",
             "summary" : "plaintext/binary",
             "description" : """
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                    sunt in culpa qui officia deserunt mollit anim id est laborum.
             """,}    
CONFIG_FILES.append(dict_file)

dict_file = {"name" : "network", 
             "path" : "/etc/sysconfig/",
             "summary" : "plaintext/binary",
             "description" : """
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                    sunt in culpa qui officia deserunt mollit anim id est laborum.
             """,}    
CONFIG_FILES.append(dict_file)

dict_file = {"name" : "ifcfg-eth0", 
             "path" : "/etc/sysconfig/network-scripts/",
             "summary" : "plaintext/binary",
             "description" : """
                    Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                    sunt in culpa qui officia deserunt mollit anim id est laborum.
             """,}    
CONFIG_FILES.append(dict_file)


PROFILE = {"HEADER" : HEADER,
           "CONFIG_FILES" : CONFIG_FILES,}

