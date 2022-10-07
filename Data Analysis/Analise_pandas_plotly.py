#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 00:53:45 2022

@author: rodrigoborneo
"""

# Passo 1: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("telecom_users.csv")

# Passo 2: Visualizar a base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)
display(tabela)
# - Entender quais as informações tão disponíveis
# - Descobrir as cagadas da base de dados

# Passo 3: Tratamento de dados
# - Valores que estão reconhecidos de forma errada
"""
há alguns erros na tabela, ex.: a coluna TotalGasto está sendo reconhecida como texto,
porém, essa contem números. Assim sendo é necessário fazer a alteração do tipo
"""

#pega a coluna TotalGasto e muda do tipo object para o tipo numeric
#o coerce é para forçar a conversão, pois em ele o Python reclama que não pode coverter string
#caso houvesse um valor dentro da coluna que não seja um número será convertido para vazio NaN
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce")

# - Valores vazios
# deletando as colunas vazias(ex.: coluna Codigo que está com NaN)
# axis = 0 _> linha ou axis = 1 _> coluna
tabela = tabela.dropna(how="all", axis=1)

# deletando as linhas vazias(caso haja algum valor NaN na linha, essa será deletada)
tabela = tabela.dropna(how="any", axis=0)
print(tabela.info())

# Passo 4: Análise Inicial
# Como estão os nossos cancelamentos? (conta os valores)
print(tabela["Churn"].value_counts())

#apresenta os valores como porcentagem com 1 casa decimal após a vírgula
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Passo 5: Análise Mais completa
# comparar cada coluna da minha tabela com a coluna de cancelamento
import plotly.express as px


"""
cria um gráfico do tipo histogram
pega a coluna de Casado para apresentar os dados
Pinta de cor diferente a coluna de Churn(quem é casado e cancelou)
text_auto mostra o número das colunas
"""
#grafico = px.histogram(tabela, x= "Casado", color="Churn", text_auto=True)


# etapa 1: criar o gráfico
"""
#O laço de repetição for serve para pegar todas as colunas da tabela e criar gráficos para ele,
pois para cada coluna na minha tabela, quero criar um gráfico 
"""
for coluna in tabela.columns:
    # para edições nos gráficos: https://plotly.com/python/histograms/
    # para mudar a cor do gráfico , color_discrete_sequence=["blue", "green"]
    grafico = px.histogram(tabela, x=coluna, color="Churn", text_auto=True)
    # etapa 2: exibir o gráfico
    grafico.show()
