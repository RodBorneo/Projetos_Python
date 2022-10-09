#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 16:52:38 2022

@author: rodrigoborneo


 -> O objetivo é conseguir prever as vendas que vamos ter em determinado período 
 com base nos gastos em anúncios nas 3 grandes redes que a empresa investe: TV, Jornal e Rádio
 
 Obs.:
 TV, Jornal e Rádio estão em milhares de reais
 Vendas estão em milhões


caso não haja, instalar:
pip install matplotlib
pip install seaborn
pip install scikit-learn
"""

import pandas as pd

tabela = pd.read_csv("advertising.csv")
display(tabela)

"""
técnicas de encoding para usar texto para treinar a IA

dummies
one hot encoding
"""

# outra forma de ver a mesma análise
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(tabela.corr(), annot=True, cmap="Wistia")
plt.show()

#sns.pairplot(tabela)
#plt.show()

from sklearn.model_selection import train_test_split

y = tabela["Vendas"]
x = tabela.drop("Vendas", axis=1) #remove a tabela de indice que não é interessante para a análise

#test_size representa a proporção do conjunto de dados a ser incluído no teste.
# Varia de 0.0(sendo nada) até 1.0 (sendo o total)

#random_state Controla o embaralhamento aplicado aos dados antes de aplicar a divisão em parte para teste e treino.

#train_size representam a proporção do conjunto de dados a ser incluído na parte de treino. 
#Se Nenhum, o valor é definido automaticamente para o complemento do tamanho do teste.

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# cria as inteligencias aritificiais
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()

# treina as inteligencias artificias
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

from sklearn import metrics

# criar as previsoes
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)

# comparar os modelos
print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_arvoredecisao))  

tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

plt.figure(figsize=(15,6)) #para aumentar o tamanho do gráfico
sns.lineplot(data=tabela_auxiliar)
plt.show()

# Como fazer uma nova previsao?
# importar a nova_tabela com o pandas (a nova tabela tem que ter os dados de TV, Radio e Jornal)

#digamos que eu invista tanto em TV, tanto em rádio, tanto em jornal
#quanto que é esperado que eu tenha de vendas
nova_tabela = pd.read_csv("novos.csv") 
display(nova_tabela)


#mostra o valor esperado que eu venha a ter de venda
#linha 0 -> vende 7.773 | linha 1 -> vende 8.819 | linha 2 -> vende 19.915
previsao = modelo_arvoredecisao.predict(nova_tabela)
print(previsao)

sns.barplot(x=x_treino.columns, y=modelo_arvoredecisao.feature_importances_)
plt.show()

# Caso queira comparar Radio com Jornal
# print(df[["Radio", "Jornal"]].sum())