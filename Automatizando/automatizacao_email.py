#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 00:26:59 2022

@author: rodrigoborneo

Executado no jupyter notebook
"""

import pyautogui
import pyperclip
import time

pyautogui.PAUSE = 1

# pyautogui.click -> clicar
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> conjunto de teclas
# pyautogui.write -> escreve um texto

# Passo 1: Entrar no sistema da empresa (link)
pyautogui.hotkey("command", "t")
pyperclip.copy("link do sistema que deseja acessar")
pyautogui.hotkey("command", "v")
pyautogui.press("enter")


#faz o reconehcimento de uma imagem na tela otimizando o tempo de espera 
#a imagem deve estar na mesma pasta onde está o código
while not pyautogui.locateOnScreen('logo_drive.png',confidence=0.9):
    time.sleep(1)

# Passo 2: Navegar no sistema e encontrar a base de vendas (entrar na pasta exportar)
pyautogui.click(x=398, y=308, clicks=2,interval=1)
pyautogui.press("enter")

# Passo 3: Fazer o download da base de vendas
pyautogui.click(x=381, y=342)# clicar no arquivo
pyautogui.click(x=1232, y=198)# clicar nos 3 pontinhos
pyautogui.click(x=997, y=601)# clicar no fazer download
time.sleep(5) # esperar o download acabar

# Passo 4: Importar a base de vendas pro Python
import pandas as pd

tabela = pd.read_excel(r"local na máquina onde está salvo o arquivo")
display(tabela)

# Passo 5: Calcular os indicadores da empresa
faturamento = tabela["Valor Final"].sum()
print(faturamento)
quantidade = tabela["Quantidade"].sum()
print(quantidade)

# Passo 6: Enviar um e-mail para a diretoria com os indicadores de venda

# abrir aba
pyautogui.hotkey("command", "t")

# entrar no link do email 
pyperclip.copy("link do e-mail ")
pyautogui.hotkey("command", "v")
pyautogui.press("enter")
time.sleep(5)

# clicar no botão escrever
pyautogui.click(x=235, y=177)

# preencher as informações do e-mail
pyperclip.copy("e-mail do destinatário")
pyautogui.hotkey("command", "v")



pyautogui.press("tab") # pular para o campo de assunto
pyperclip.copy("Assunto do e-mail")
pyautogui.hotkey("command", "v")

pyautogui.press("tab") # pular para o campo de corpo do email

texto = f"""

Segue relatório de vendas.
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,}

"""


# formatação dos números (moeda, dinheiro)

pyperclip.copy(texto)
pyautogui.hotkey("command", "v")

#anexar o arquivo que está na lista de sugeridos do Outlook

pyautogui.click(x=536, y=668)
time.sleep(3)
pyautogui.click(x=603, y=420)



# enviar o e-mail
pyautogui.hotkey("command", "enter")


"""
DICA

Use esse código para descobrir qual a posição de um item que queira clicar

Lembre-se: a posição na sua tela é diferente da posição na minha tela

time.sleep(5)
pyautogui.position()

"""