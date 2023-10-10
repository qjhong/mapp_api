# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 14:27:40 2023

@author: qhong7
"""

import pandas as pd
df_formula = pd.read_csv('chemical_formula.csv', names=['chemical_formula'])

data_str = "["
for i in range(df_formula.shape[0]):
    if len(data_str) > 2: data_str += ","
    data_str += '{"9":"' + df_formula.iloc[i]['chemical_formula'] + '"}'
data_str += "]"

import requests

url = 'http://206.207.50.58:5007/MT_ML_Qijun_Hong_Predict_noNN'
payload = data_str
headers = {'content-type': 'application/json'}
r = requests.post(url, data=payload, headers=headers)

df_mp = pd.DataFrame(str(r.content).split('{"melting temperature\": ')[1:], columns=['mp'])
df_mp['melting_temperature_in_kelvin'] = df_mp.apply(lambda x: float( x['mp'].split(",")[0] ), axis=1)
df_mp['standard_error_in_kelvin'] = df_mp.apply(lambda x: float( x['mp'].split(":")[1].split("}")[0] ), axis=1)

df = pd.concat([df_formula, df_mp.drop(columns='mp')], axis=1)

df.to_csv('output.csv')

'''
speed test:
10: 7s
1000: 34s
10000: 303s
'''
