from selenium import webdriver
import time as t
from selenium.webdriver.common.by import By as by
import pandas as pd
from datetime import datetime as dt
import pyautogui as pyaug
pyaug.FAILSAFE = False
def fazer_login():
    email = 'hitalo.santos@taxall.com.br'
    senha = 'S3nh@002'
    d = (dt.now().day) - 1
    m = dt.now().month
    a = dt.now().year
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    navegador.get('https://onvio.com.br/#/')
    t.sleep(1)
    navegador.find_element(by.ID, 'trauth-continue-signin-btn').click()
    t.sleep(2)
    navegador.find_element(by.ID, 'username').send_keys(email)
    navegador.find_element(by.XPATH, '//*[@id="root"]/div/div/div[2]/div/main/section/div/div/div/div[1]/div/form/div[2]/button').click()
    t.sleep(1)
    navegador.find_element(by.ID, 'password').send_keys(senha)
    navegador.find_element(by.NAME, 'action').click()
    t.sleep(5)
    navegador.find_element(by.ID, 'bm-header-app-menu-toggle').click()
    t.sleep(2)
    navegador.find_element(by.CLASS_NAME, 'bento-icon-newtab').click()
    t.sleep(3)
    handles = navegador.window_handles
    curwin = handles[-1]
    navegador.switch_to.window(curwin)
    navegador.find_element(by.XPATH, '//*[@id="custom-header"]/div[5]/div/on-nav/nav/div[2]').click()
    t.sleep(2)
    navegador.find_element(by.CLASS_NAME, 'on-nav__child.ng-star-inserted').click()
    t.sleep(2)
    navegador.find_element(by.CLASS_NAME, 'btn.btn-outline-primary.btn-icon.btn-toggle').click()
    t.sleep(1)
    navegador.find_element(by.XPATH, '//*[@id="gridServiceRequestList"]/div[1]/div[5]/div/div[1]/div[4]/div/input').click()
    navegador.find_element(by.XPATH, '//*[@id="gridServiceRequestList"]/div[1]/div[5]/div/div[1]/div[4]/div/input').send_keys(d, m, a)
    navegador.find_element(by.XPATH, '//*[@id="query-combobox-2"]').click()
    navegador.find_element(by.XPATH, '//*[@id="query-combobox-2"]').send_keys('Contabilidade')
    t.sleep(1)
    pyaug.press("down")
    pyaug.press("enter")
    navegador.find_element(by.XPATH, '//*[@id="items-per-page-0"]').click()
    pyaug.press("down")
    pyaug.press("down")
    pyaug.press("down")
    pyaug.press("enter")
    t.sleep(5)
    
    qnt = navegador.find_element(by.XPATH, '//*[@id="custom-header"]/div[5]/div/main/app-general-request-container/div/app-general-request-list/div/div[2]/bento-pagination/nav/div[2]/div[1]').text
    qnt = qnt.split()
    qnt = qnt[3]
    qnt = int(qnt)

    dadostabela = []    
    x = 2
    for i in range(qnt):
        dadoslinha = []
        linha = navegador.find_element(by.XPATH, f'//*[@id="gridServiceRequestList"]/div[1]/div[1]/div[1]/div[{x}]').text
        dadoslinha.append(linha)
        x += 1
        dadostabela.append(dadoslinha)

    pag = navegador.find_element(by.XPATH, '//*[@id="custom-header"]/div[5]/div/main/app-general-request-container/div/app-general-request-list/div/div[2]/bento-pagination/nav/div[1]/div[1]/div[1]').text
    pag = pag.split()
    if pag[1] != pag[-1]:
        navegador.find_element(by.CLASS_NAME, 'btn.btn-outline-primary.btn-icon').click()
        for i in range(2, qnt):

            dadoslinha = []
            linha = navegador.find_element(by.XPATH, f'//*[@id="gridServiceRequestList"]/div[1]/div[1]/div[1]/div[{x}]').text
            
            dadoslinha.append(linha)
            x += 1
            dadostabela.append(dadoslinha)
            
    nomes_cabecalho = navegador.find_element(by.XPATH, '//*[@id="gridServiceRequestList"]/div[1]/div[5]/div/div[2]').text
    nomes_cabecalho = nomes_cabecalho.split('\n')
    df = []

    for lista in dadostabela:
        lista = lista[0]
        lista = lista.split('\n') 
        df.append(lista)      
    

    df_final = pd.DataFrame(df)
    df_final.columns = nomes_cabecalho
    df_final.drop(columns=['Ações'], inplace=True)
    df_final.to_excel('Login, coleta de dados e exportação para exel\Solicitações Gerais (Contabilidade).xlsx', index=False)

    navegador.close()
fazer_login()