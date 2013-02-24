#!/usr/bin/env python
# encoding: utf-8
from lib.utils import getFileList

# Configs para Geral
# Arquivos de configuração

HEADER = {"name" : "Geral",
          "description" : "Perfil de configuração geral",
          "icon" : "zeus.gif",}

file_list = getFileList("/Zanthus/Zeus/pdvJava/")

CONFIG_FILES = []
for filename in file_list:
    dict_file = {"name" : filename, 
            "path" : "/Zanthus/Zeus/pdvJava/",
            "summary" : "Arquivo de configuração",
            "description" : """
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut 
                enim ad minim veniam, quis nostrud exercitation ullamco laboris 
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
                reprehenderit in voluptate velit esse cillum dolore eu fugiat 
                nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
                sunt in culpa qui officia deserunt mollit anim id est laborum.
            """,}    
    CONFIG_FILES.append(dict_file)
    

ECF9CFG = {"name" : "ECF9.CFG",
           "path" : "/Zanthus/Zeus/pdvJava",
           "summary" : "Arquivo de configuração",
           "description" : """
               Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
               eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut 
               enim ad minim veniam, quis nostrud exercitation ullamco laboris 
               nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
               reprehenderit in voluptate velit esse cillum dolore eu fugiat 
               nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
               sunt in culpa qui officia deserunt mollit anim id est laborum.
           """,}


PROFILE = {"HEADER" : HEADER,
           "CONFIG_FILES" : CONFIG_FILES,}

