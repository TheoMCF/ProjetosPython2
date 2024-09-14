import os
import qrcode as qr
from selenium import webdriver
from selenium.webdriver.common.by import By as by
import time as t
from pyautogui import doubleClick
from pyautogui import typewrite
from pyautogui import press
from pyautogui import click
from pyautogui import hotkey

# Lista os nomes dos PDFs 
nomes_pdfs = os.listdir('Pdf to QRCODE\pdfs')
x = 0

# Reseta a variável x para iniciar a lista de nomes dos PDFs de novo
def reset_X():
    global x
    x = 0

# Retira a parte ".pdf" do nome dos arquivos
for i in range(1, len(nomes_pdfs) + 1):
    nomes_pdfs[x] = nomes_pdfs[x].replace('.pdf', '')
    x += 1

reset_X()

# Converte cada PDF para QRCode
def pdf_to_qrcode():
    global x
    navegador = webdriver.Chrome()
    navegador.maximize_window()
    navegador.get('https://me-qr.com/qr-code-generator/pdf') # Site do conversor
    t.sleep(5)
    navegador.find_element(by.XPATH, '//*[@id="root"]/div[2]/div/section/div/form/div[1]/div[1]/div/div/div[1]').click()
    t.sleep(5)
    click(81, 382)
    t.sleep(1)
    doubleClick(485, 187)
    t.sleep(1)
    typewrite('pdf')
    t.sleep(1)
    press('enter')
    t.sleep(1)
    press('p')
    t.sleep(1)
    press('enter')
    t.sleep(1)
    typewrite(nomes_pdfs[x])
    t.sleep(1)
    click(789, 509)
    navegador.find_element(by.XPATH, '//*[@id="root"]/div[2]/div/section/div/form/div[2]/div[1]/div/div/input').send_keys(nomes_pdfs[x])
    x += 1
    t.sleep(5)
    navegador.find_element(by.XPATH, '//*[@id="secondStepClick"]').click()
    t.sleep(2)
    navegador.find_element(by.XPATH, '//*[@id="downloadQrCode"]').click()
    t.sleep(5)
    navegador.close()

# Move os QrCodes para uma pasta separada
def store_qr_codes():
    global x
    press('win')
    t.sleep(1)
    typewrite('file')
    t.sleep(1)
    press('enter')
    t.sleep(5)
    click(93, 295) #Clica na pasta downloads
    t.sleep(1)
    click(1544, 63) #Clica na caixa de pesquisa
    typewrite(nomes_pdfs[x])
    x += 1
    t.sleep(3)
    click(375, 214) #Clica no primeiro arquivo
    hotkey('ctrl', 'x')
    click(93, 295)
    t.sleep(1)
    click(1544, 63)
    t.sleep(1)
    typewrite('QrCodes')
    t.sleep(3)
    doubleClick(375, 214)
    t.sleep(2)
    click(228,117)
    t.sleep(1)
    hotkey('alt', 'f4')

# Executa a primeira função para cada pdf na lista de pdfs
for i in range(1, len(nomes_pdfs) + 1):
    pdf_to_qrcode()
    t.sleep(5)
reset_X()

# Executa a segunda função para cada qrcode convertido
for i in range(1, len(nomes_pdfs) + 1):
    store_qr_codes()
    t.sleep(5)

