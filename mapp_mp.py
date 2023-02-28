#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 12:57:55 2023

@author: qhong7
"""

import pandas as pd
import os
comm = """curl --request POST 
        --url "http://206.207.50.58:5007/MT_ML_Qijun_Hong_Predict_noNN" 
        --header "content-type:application/json" 
        --data """

df_formula = pd.read_csv('chemical_formula.csv', names=['chemical_formula'])

data_str = "\'["
for i in range(df_formula.shape[0]):
    if len(data_str) > 2: data_str += ","
    data_str += '{"9":"' + df_formula.iloc[i]['chemical_formula'] + '"}'
data_str += "]\'"
comm +=  data_str + "> predictions "

response = os.system(comm.replace('\n',''))
os.system("""cat predictions | sed 's/,/\\n/g' | cut -d':' -f2 | sed 's/}//' | sed 's/]//' > predictions.csv""")

'''
speed test:
10: 7s
1000: 34s
10000: 303s
'''

df_mp = pd.read_csv('predictions.csv', names=['melting_temperature_in_Kelvin'])
df = pd.concat([df_formula, df_mp], axis=1)

df.to_csv('output.csv')
os.system("""rm predict*""")
