import streamlit as st
import os
from docx import Document as doc
con_clube = doc('Manipulação de contratos/Contratos/CONTRATO - CLUBE.docx')
con_domestica = doc('Manipulação de contratos/Contratos/CONTRATO - DOMESTICA.docx')
con_padrao = doc('Manipulação de contratos/Contratos/CONTRATO - PADRAO.docx')
con_permuta = doc('Manipulação de contratos/Contratos/CONTRATO - PERMUTA.docx')


campos_contrato_final = []
st.set_page_config(page_title='Preencher Contratos Fácil e Rápido.com.br')
listaaquivos = os.listdir('Manipulação de contratos\Contratos')

st.subheader('Contratos disponíveis:')
ce = st.selectbox(label='Contratos:', options=listaaquivos)
confirmar = st.button(label='Confirmar') 

if confirmar == True:

    RAZAO_SOCIAL = st.text_input('RAZAO_SOCIAL')
    CNPJ_CONTRATANTE = st.text_input('CNPJ_CONTRATANTE')
    CEP_EMPRESA = st.text_input('CEP_EMPRESA')
    ENDERECO_EMPRESA = st.text_input('ENDERECO_EMPRESA')
    NOME_AVALISTA = st.text_input('NOME_AVALISTA')
    CPF_AVALISTA = st.text_input('CPF_AVALISTA')
    ENDERECO_AVALISTA = st.text_input('ENDERECO_AVALISTA')
    CEP_AVALISTA = st.text_input('CEP_AVALISTA')
    VALOR_MENSAL = st.text_input('VALOR_MENSAL')
    VALOR_POR_EXTENSO = st.text_input('VALOR_POR_EXTENSO')
    QTD_FUNC = st.text_input('QTD_FUNC')
    VALOR_FUNC = st.text_input('VALOR_FUNC')
    VALOR_POR_EXTENSO_FUNC = st.text_input('VALOR_POR_EXTENSO_FUNC')
    REGIME = st.text_input('REGIME')
    QTD_FISCAL = st.text_input('QTD_FISCAL')
    QTD_CONTABIL = st.text_input('QTD_CONTABIL')
    VENCIMENTO = st.text_input('VENCIMENTO')
    DATA_VIGENCIA = st.text_input('DATA_VIGENCIA')
    DATA_ASSINATURA = st.text_input('DATA_ASSINATURA')

    campos_contrato = [
    RAZAO_SOCIAL,
    CNPJ_CONTRATANTE,
    CEP_EMPRESA,
    ENDERECO_EMPRESA,
    NOME_AVALISTA,
    CPF_AVALISTA,
    ENDERECO_AVALISTA,
    CEP_AVALISTA,
    VALOR_MENSAL,
    VALOR_POR_EXTENSO,
    QTD_FUNC,
    VALOR_FUNC,
    VALOR_POR_EXTENSO_FUNC,
    REGIME,
    QTD_FISCAL,
    QTD_CONTABIL,
    VENCIMENTO,
    DATA_VIGENCIA,
    DATA_ASSINATURA
]

def contrato_clube():    
    preencher = st.button(label='Preencher Contrato')
    if preencher == True:
        for campo in campos_contrato:
            if campo == '':
                st.error('Todos os campos devem estar preenchidos.')
                preencher == False
                preencher = st.button(label='Tentar Novamente')

            if campo != '':
                campos_contrato_final.append()
        x = 0
        for paragrafo in con_clube.paragraphs:
            paragrafo.text = paragrafo.text.replace("{{", '')
            paragrafo.text = paragrafo.text.replace("}}", '')
            paragrafo.text = paragrafo.text.replace(f'{campos_contrato[x]}', f'{campos_contrato_final[x]}') 
            
            if x < 18:
                x += 1
    Salvar_Contrato = st.button(label='Salvar Contrato')
    if Salvar_Contrato == True:
        con_clube.save("Manipulação de contratos\ CONTRATO  PREENCHIDO- CLUBE.docx")
def contrato_domestica():
    preencher = st.button(label='Preencher Contrato')
    if preencher == True:
        for campo in campos_contrato:
            if campo == '':
                st.error('Todos os campos devem estar preenchidos.')
                preencher == False
                preencher = st.button(label='Tentar Novamente')

            if campo != '':
                campos_contrato_final.append()
        x = 0
        for paragrafo in con_clube.paragraphs:
            paragrafo.text = paragrafo.text.replace("{{", '')
            paragrafo.text = paragrafo.text.replace("}}", '')
            paragrafo.text = paragrafo.text.replace(f'{campos_contrato[x]}', f'{campos_contrato_final[x]}') 
            
            if x < 18:
                x += 1
    Salvar_Contrato = st.button(label='Salvar Contrato')
    if Salvar_Contrato == True:
        con_domestica.save("Manipulação de contratos\ CONTRATO PREENCHIDO - DOMESTICA.docx")
def contrato_padrão():
    preencher = st.button(label='Preencher Contrato')
    if preencher == True:
        for campo in campos_contrato:
            if campo == '':
                st.error('Todos os campos devem estar preenchidos.')
                preencher == False
                preencher = st.button(label='Tentar Novamente')

            if campo != '':
                campos_contrato_final.append()
        x = 0
        for paragrafo in con_clube.paragraphs:
            paragrafo.text = paragrafo.text.replace("{{", '')
            paragrafo.text = paragrafo.text.replace("}}", '')
            paragrafo.text = paragrafo.text.replace(f'{campos_contrato[x]}', f'{campos_contrato_final[x]}') 
            
            if x < 18:
                x += 1
    Salvar_Contrato = st.button(label='Salvar Contrato')
    if Salvar_Contrato == True:        con_padrao.save("Manipulação de contratos\ CONTRATO PREENCHIDO - PADRAO.docx")
def contrato_permuta():
    preencher = st.button(label='Preencher Contrato')
    if preencher == True:
        for campo in campos_contrato:
            if campo == '':
                st.error('Todos os campos devem estar preenchidos.')
                preencher == False
                preencher = st.button(label='Tentar Novamente')

            if campo != '':
                campos_contrato_final.append()
        x = 0
        for paragrafo in con_clube.paragraphs:
            paragrafo.text = paragrafo.text.replace("{{", '')
            paragrafo.text = paragrafo.text.replace("}}", '')
            paragrafo.text = paragrafo.text.replace(f'{campos_contrato[x]}', f'{campos_contrato_final[x]}') 
            
            if x < 18:
                x += 1
    Salvar_Contrato = st.button(label='Salvar Contrato')
    if Salvar_Contrato == True:
        con_permuta.save("Manipulação de contratos\ CONTRATO PREENCHIDO - PERMUTA.docx")

if ce == listaaquivos[0]:
    if confirmar == True:
        contrato_clube()
elif ce == listaaquivos[1]:
    if confirmar == True:
        contrato_domestica()
elif ce == listaaquivos[2]:
    if confirmar == True:
        contrato_padrão()
else:
    if confirmar == True:
        contrato_permuta()