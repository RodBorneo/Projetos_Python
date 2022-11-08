#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 2022

@author: rodrigoborneo

Qual a maior altura, o maior peso, a menor altura e menor peso?
Qual é o estado onde nasce o maior número de jogadores?
Qual o jogador mais alto?
"""

import pandas as pd


file = 'datasets_1358_30676_Players.csv'

df = pd.read_csv(file)

#Qual a média de altura e de peso dos jogadores?
print("média das alturas:",df['height'].mean(),"\n")


print("média dos pesos:",df['weight'].mean(),"\n")

#Crie uma nova coluna com a razão peso/altura.
IMC = df['weight']/((df['height']/100)**2)


df['IMC'] = IMC

#print(df.head())

print("menor altura =", df.height.min(),"\n")
print("menor peso =", df.weight.min(),"\n")

print("Qauntidade de jogadores por estado/país:")

print(df['birth_state'].value_counts(),"\n")

#print("Jogador mais alto:",df.sort_values(by='height').tail(2))

#pega os 20 primeiros da coluna nome ate a coluna weight
print(df.iloc[0:20,1:4])