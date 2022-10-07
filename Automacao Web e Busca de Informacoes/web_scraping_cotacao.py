import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para apertar teclas
from selenium.webdriver.common.by import By

# para rodar o firefox em 2º plano
#from selenium.webdriver.firefox.options import Options
#firefox_options = Options()
#firefox_options.headless = True 
# navegador = webdriver.Firefox(options=chrome_options)

# abrir um navegador
navegador = webdriver.Firefox(executable_path = '/usr/local/bin/geckodriver')
# caso queira deixar na mesma pasta do seu código
# navegador = webdriver.Chrome("chromedriver.exe")


navegador.get("https://www.google.com/")

# Passo 1: Pegar a cotação do Dólar
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação dólar")

navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

time.sleep(10) # ta tentando pegar antes de carregar
cotacao_dolar = navegador.find_element(By.XPATH,
    '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute("data-value") 
print(cotacao_dolar)

# Passo 2: Pegar a cotação do Euro
navegador.get("https://www.google.com/")
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
navegador.find_element(By.XPATH,
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

time.sleep(10)
cotacao_euro = navegador.find_element(By.XPATH,
    '/html/body/div[7]/div/div[10]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[3]/div[1]/div[1]/div[2]/span[1]').get_attribute("data-value")
print(cotacao_euro)

# Passo 3: Pegar a cotação do Ouro
navegador.get("https://www.melhorcambio.com/ouro-hoje")

cotacao_ouro = navegador.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",", ".")
print(cotacao_ouro)

# Passo 4: Importar a lista de produtos
import pandas as pd

tabela = pd.read_excel("Produtos.xlsx")
display(tabela)

# Passo 5: Recalcular o preço de cada produto
# atualizar a cotação
# nas linhas onde na coluna "Moeda" = Dólar
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação"] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação"] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação"] = float(cotacao_ouro)

# atualizar o preço base reais (preço base original * cotação)
tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]

#atualizar o preço final (preço base reais * Margem)
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

#formata para o valor ficar com 2 casas decimais
tabela["Preço de Venda"] = tabela["Preço de Venda"].map("R${:.2f}".format)
display(tabela)

# Passo 6: Salvar os novos preços dos produtos
#index=False é para excluir a primeira coluna, pois essa é inútil
tabela.to_excel("Produtos Atualizado.xlsx", index=False)

navegador.quit()