#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:47:15 2023

@author: qhong7
"""

import pandas as pd

#list_formula = ['Hf_1C_0.5N_0.3','SiO2','La2Zr2O7','Hg']
list_formula = []
l = len(list_formula)
if l == 0:
    df = pd.read_csv('chemical_formula.csv', names=['chemical_formula'])
    list_formula = df.applymap(str)['chemical_formula'].tolist()
    l = len(list_formula)

data_str = "["
for i in range(len(list_formula)):
    if len(data_str) > 2: data_str += ","
    data_str += '{"9":"' + list_formula[i] + '"}'
data_str += "]"

import requests

url = 'http://206.207.50.58:5008/MT_ML_Qijun_Hong_Predict'
payload = data_str
headers = {'content-type': 'application/json'}
r_bm = requests.post(url, data=payload, headers=headers)

url = 'http://206.207.50.58:5009/MT_ML_Qijun_Hong_Predict'
r_vl = requests.post(url, data=payload, headers=headers)

url = 'http://206.207.50.58:5006/MT_ML_Qijun_Hong_Predict'
r_mp = requests.post(url, data=payload, headers=headers)

##%%
bm, vl, mp = [],[],[]
for i in range(l):
    print('The chemical formula is \t\t', list_formula[i])
    bulk_modulus_in_GPa = str(r_bm.content).split('{"melting temperature\": ')[1:][i].split("}")[0]
    volume_in_ang3_per_atom = str(r_vl.content).split('{"melting temperature\": ')[1:][i].split("}")[0]
    melt_temp_in_kelvin = str(r_mp.content).split('{"melting temperature\": ')[1:][i].split("}")[0]
    print('Melting temperature is\t\t', "{:.0f}".format(float(melt_temp_in_kelvin)), ' K')
    print('Bulk modulus is  \t\t\t', "{:.0f}".format(float(bulk_modulus_in_GPa)), ' GPa')
    print('Volume is   \t\t\t\t\t', "{:.2f}".format(float(volume_in_ang3_per_atom)), ' Ang^3/atom')
    print('')
    bm.append(bulk_modulus_in_GPa)
    vl.append(volume_in_ang3_per_atom)
    mp.append(melt_temp_in_kelvin)
    
##%%
df_mp = pd.DataFrame(mp, columns=['melt_temp_in_kelvin'])
df_vl = pd.DataFrame(vl, columns=['volume_in_ang3_per_atom'])
df_bm = pd.DataFrame(bm, columns=['bulk_modulus_in_GPa'])
df = pd.concat([df, df_mp, df_vl, df_bm], axis=1)
df.to_csv('output.csv')

