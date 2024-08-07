import pyodbc as py
import streamlit as st
import pandas as pd
import time


dados_conexao = (
    "Driver={SQL Server};"
    "Server=wiliam;"
    "Database=PythonSQL;"
)

conexao = py.connect(dados_conexao)
cursor = conexao.cursor()

st.set_page_config(page_title='CRUD.com')
st.title('Manilpulação de Dados SQL')
choice = st.radio("O Que você quer fazer na tabela?", ["Visualizar Tabela","Adicionar Valores" ,"Mudar Valores", "Deletar Valores",])

def adicionar_valores():

    st.subheader("Preencha os dados para criar uma nova venda:")
    # if 'cliente' not in st.session_state:
    #     st.session_state.cliente = ''
    cliente = st.text_input("Nome do cliente: ")
    produto = st.text_input("Produto: ")
    data_venda = str(st.date_input('Data da venda: '))      
    preco = st.text_input('Preço do produto: ')
    quantidade = st.number_input('Quantidade de produtos: ', 0)
    
    confirmar = st.button('Confirmar')
    
    if confirmar:
        preco = float(preco)
        comando = f"INSERT INTO vendas (cliente, produto, data_venda, preco, quantidade) VALUES ('{cliente}', '{produto}', '{data_venda}', {preco}, {quantidade})"
        cursor.execute(comando)
        conexao.commit()
        st.success('Conexão Concluida!')
def visualizar_tabela():
        clientes = []
        produtos = []
        datas = []
        precos = []
        quantidade = []

        comando = 'SELECT * FROM vendas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for row in resultado:
            clientes.append(row[0]) 
            produtos.append(row[1])
            datas.append(row[2])
            precos.append(row[3])
            quantidade.append(row[4])
        tr = len(resultado) + 1

        df1 = pd.DataFrame()
        j = 0
        for i in range(1,tr):
            linha = {"Cliente": f"{clientes[j]}", "Produto": f"{produtos[j]}", "Data da venda": f"{datas[j]}", "Preço" : f"{precos[j]}", "Quantidade" : f"{quantidade[j]}"}
            df1 = df1._append(linha, ignore_index = True)
            j +=1
        st.dataframe(df1)

if choice == "Adicionar Valores":
    adicionar_valores()
        
elif choice == "Visualizar Tabela":
    visualizar_tabela()
    

