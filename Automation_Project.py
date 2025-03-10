#Passo a passo:
#Entrar no site da empresa 
#Logar
#Importar os produtos para cadatro
#Cadastrar os produtos 
#Repetir a sequência 

import pyautogui
import time
import pandas 

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)

pyautogui.click(x=737, y=371)
pyautogui.write("jornadapythonteste@gmai.com")
pyautogui.press("tab")
pyautogui.write("123456789.")
pyautogui.press("enter")

time.sleep(4)
tabela = pandas.read_csv("produtos.csv")

for linha in tabela.index:
    
    pyautogui.click(x=601, y=262)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    else:
      pyautogui.write("Nada aqui")
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)
    
