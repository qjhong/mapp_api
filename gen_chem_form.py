#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 13:10:30 2023

@author: qhong7
"""

import pandas as pd

def part2formula(part,conc):
    chem_form = ''
    for key in part.keys():
        chem_form += key
        chem_form += '_'
        chem_form += str(conc*part[key])
    return chem_form

part1 = {'Si':1,'O':2}
part2 = {'Th':1,'O':2}
n = 100
chem_form_list = []
chem_form_list.append( part2formula(part2,1.0) )
for i in range(n+1):
    chem_form_list.append( part2formula(part1,float(i)/n) + part2formula(part2,float(n-i)/n) )
chem_form_list.append( part2formula(part1,1.0) )

df = pd.DataFrame(chem_form_list)

df.to_csv('chemical_formula.csv',index=False,header=False)
