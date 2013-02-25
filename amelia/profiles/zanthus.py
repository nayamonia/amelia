#!/usr/bin/env python
# encoding: utf-8
from lib.utils import getIFileList

# Configs para PDV Zanthus
# Arquivos de configuração

HEADER = {"name" : "Zanthus",
          "description" : "Arquivos de configuração das pastas pdvJava e pdvGUI",
          "icon" : "zeus.gif",}

CONFIG_FILES = []

dir_list, file_list = getIFileList("/Zanthus/Zeus/pdvJava/")
for filename, mime_type in file_list:
    if "application" not in mime_type and\
       "xml" not in mime_type and\
       ".ZMV" not in filename and\
       ".ZLZ" not in filename:
        dict_file = {"name" : filename, 
                     "path" : "/Zanthus/Zeus/pdvJava/",
                     "summary" : mime_type,
                     "description" : """
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                            sunt in culpa qui officia deserunt mollit anim id est laborum.
                     """,}    
        CONFIG_FILES.append(dict_file)

dir_list, file_list = getIFileList("/Zanthus/Zeus/pdvJava/pdvGUI/")
for filename, mime_type in file_list:
    if "application" not in mime_type and\
       "xml" not in mime_type and\
       ".ZMV" not in filename and\
       ".ZLZ" not in filename:
        dict_file = {"name" : filename, 
                     "path" : "/Zanthus/Zeus/pdvJava/pdvGUI/",
                     "summary" : mime_type,
                     "description" : """
                            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                            sunt in culpa qui officia deserunt mollit anim id est laborum.
                     """,}    
        CONFIG_FILES.append(dict_file)

PROFILE = {"HEADER" : HEADER,
           "CONFIG_FILES" : CONFIG_FILES,}
