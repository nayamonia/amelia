#!/usr/bin/env python
# encoding: utf-8

# Configs para PDV Zanthus

# Arquivos de configuração

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

ECF9FCFG = {"name" : "ECF9F.CFG",
            "path" : "/Zanthus/Zeus/pdvJava",
            "summary" : "Arquivo de configuração F",
            "description" : """
                Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do 
                eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut 
                enim ad minim veniam, quis nostrud exercitation ullamco laboris 
                nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
                reprehenderit in voluptate velit esse cillum dolore eu fugiat 
                nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
                sunt in culpa qui officia deserunt mollit anim id est laborum.
            """,}

CONFIG_FILES = [ECF9CFG, ECF9FCFG]

HEADER = {"name" : "Zanthus2",
          "description" : "Perfil de configuração padrão alternativo",
          "icon" : "zeus.gif",}

PROFILE = {"HEADER" : HEADER,
           "CONFIG_FILES" : CONFIG_FILES,}
