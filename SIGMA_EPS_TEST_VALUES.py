#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 16:19:45 2021

@author: joe
"""
import os
import numpy as np
import pandas as pd
import math
import itertools
#os.system("ls")

import subprocess # just to call an arbitrary command e.g. 'ls'

import os

class cd:
    """Context manager for changing the current working directory"""
    def __init__(self, newPath):
        self.newPath = os.path.expanduser(newPath)

    def __enter__(self):
        self.savedPath = os.getcwd()
        os.chdir(self.newPath)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.savedPath)
##############################################################################
def create_bash(S):
    with open ('bash.sh', 'w') as rsh:
        rsh.write(f'''#!/bin/bash \nsed -i 's/XXXXXXXXXXXXXXXXXXXXXXX/{S}/g' ffnonbonded.itp
        ''')
###############################################################################
os.system("rm -r 0*")
Sigma = [0,0.1,0.2,0.3,0.4,0.5]
Epsilon = [0,0.5,1.0,1.5,2.0,2.5]

Both = list(itertools.product(Sigma, Epsilon))
#print(Both)
###############################################################################

for n,i in enumerate(Both):
    se = (Both[n])
    name = str(se[0]) + "_" + str(se[1])
    #print(str(name))
    os.system("cp -r original %s" %name)
    S = se[0]
    S =str("%.12f") %(S)
    E = se[1]
    E =str("%.4f") %(E)
    print(S,E)
    WD = "~/PSEUDO/%s/GolP-charmm36-mar2019.ff" %(name)
    #print(WD)
    # enter the directory like this:



    with cd(WD):
       subprocess.call("pwd")
       #os.system('ls')
       print(S, E)
       SE = (str(S)+("  ")+(str(E)))
       print(SE)
       create_bash(SE)
       os.system("bash bash.sh")
       os.system("insert gromacs here")
