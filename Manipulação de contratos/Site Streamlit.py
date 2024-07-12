import streamlit as st
import os
from docx import Document as doc
con_clube = doc('Manipulação de contratos/Contratos/CONTRATO - CLUBE.docx')
con_domestica = doc('Manipulação de contratos/Contratos/CONTRATO - DOMESTICA.docx')
con_padrao = doc('Manipulação de contratos/Contratos/CONTRATO - PADRAO.docx')
con_permuta = doc('Manipulação de contratos/Contratos/CONTRATO - PERMUTA.docx')

campos_contrato = [
'RAZAO_SOCIAL',
'CNPJ_CONTRATANTE',
'CEP_EMPRESA',
'ENDERECO_EMPRESA',
'NOME_AVALISTA',
'CPF_AVALISTA',
'ENDERECO_AVALISTA',
'CEP_AVALISTA',
'VALOR_MENSAL',
'VALOR_POR_EXTENSO',
'QTD_FUNC',
'VALOR_FUNC',
'VALOR_POR_EXTENSO_FUNC',
'REGIME',
'QTD_FISCAL',
'QTD_CONTABIL',
'VENCIMENTO',
'DATA_VIGENCIA',
'DATA_ASSINATURA'
]

st.set_page_config(page_title='Preencher Contratos Fácil e Rápido.com.br')
listaaquivos = os.listdir('Manipulação de contratos\Contratos')


st.subheader('Contratos disponíveis:')
ce = st.selectbox(label='Contratos:', options=listaaquivos)

y = 0
for string in campos_contrato:
    campos_contrato[y] = st.text_input(f'{campos_contrato[y]}')
    y+=1
def contrato_clube():
    x = 0
    for paragrafo in con_clube.paragraphs:
        paragrafo.text = paragrafo.text.replace("{{", '')
        paragrafo.text = paragrafo.text.replace("}}", '')
        x += 1
    botao = st.button(label='Finalizar')
    if botao == True:
        con_clube.save("Manipulação de contratos\ CONTRATO  PREENCHIDO- CLUBE.docx")
def contrato_domestica():
    x = 0
    for paragrafo in con_domestica.paragraphs:
        paragrafo.text = paragrafo.text.replace("{{", '')
        paragrafo.text = paragrafo.text.replace("}}", '')
        x += 1
    botao = st.button(label='Finalizar')
    if botao == True:
        con_domestica.save("Manipulação de contratos\ CONTRATO PREENCHIDO - DOMESTICA.docx")
def contrato_padrão():
    x = 0
    for paragrafo in con_padrao.paragraphs:
        paragrafo.text = paragrafo.text.replace("{{", '')
        paragrafo.text = paragrafo.text.replace("}}", '')
        x += 1
    botao = st.button(label='Finalizar')
    if botao == True:
        con_padrao.save("Manipulação de contratos\ CONTRATO PREENCHIDO - PADRAO.docx")
def contrato_permuta():
    x = 0
    for paragrafo in con_permuta.paragraphs:
        paragrafo.text = paragrafo.text.replace("{{", '')
        paragrafo.text = paragrafo.text.replace("}}", '')
        x += 1
    botao = st.button(label='Finalizar')
    if botao == True:
        con_permuta.save("Manipulação de contratos\ CONTRATO PREENCHIDO - PERMUTA.docx")

if ce == listaaquivos[0]:
    contrato_clube()
elif ce == listaaquivos[1]:
    contrato_domestica()
elif ce == listaaquivos[2]:
    contrato_padrão()
else:
    contrato_permuta()