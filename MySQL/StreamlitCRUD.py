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
col1, col2 = st.columns([0.4,1])

def clear_text():
    x = ''
def adicionar_valores():

    st.subheader("Preencha os dados para criar uma nova venda:")
    cliente = st.text_input("Nome do cliente: ")
    produto = st.text_input("Produto: ")
    data_venda = str(st.date_input('Data da venda: '))      
    preco = st.text_input('Preço do produto: ')
    quantidade = st.number_input('Quantidade de produtos: ', 0)
    idvenda = st.number_input('ID da venda: ', 0)
    confirmar = st.button('Confirmar')
    
    if confirmar:
        preco = float(preco)
        comando = f"INSERT INTO vendas (cliente, produto, data_venda, preco, quantidade, id_venda) VALUES ('{cliente}', '{produto}', '{data_venda}', {preco}, {quantidade}, {idvenda})"
        cursor.execute(comando)
        conexao.commit()
        st.success('Conexão Concluida!')
def visualizar_tabela():
        clientes = []
        produtos = []
        datas = []
        precos = []
        quantidade = []
        id = []
        comando = 'SELECT * FROM vendas'
        cursor.execute(comando)
        resultado = cursor.fetchall()
        for row in resultado:
            clientes.append(row[0]) 
            produtos.append(row[1])
            datas.append(row[2])
            precos.append(row[3])
            quantidade.append(row[4])
            id.append(row[5])
        tr = len(resultado) + 1

        df1 = pd.DataFrame()
        j = 0
        for i in range(1,tr):
            linha = { "ID da venda": f"{id[j]}", "Cliente": f"{clientes[j]}", "Produto": f"{produtos[j]}", "Data da venda": f"{datas[j]}", "Preço" : f"{precos[j]}", "Quantidade" : f"{quantidade[j]}"}
            df1 = df1._append(linha, ignore_index = True)
            j +=1
        st.dataframe(df1)
def mudar_valores():
    x = ''
    col_int = ["preco", "quantidade"]
    st.subheader("Preencha os dados para fazer a alteração")
    st.write('Tabela Atual:')
    visualizar_tabela()
    
    valor_antes = st.text_input('Valor a ser alterado:', key="1",value=x)
    valor_depois = st.text_input("Esse valor será subistituido por:", key="2",value=x)

    colunas = st.selectbox("Coluna onde ele está:", ("","Clientes", "Produto", "Data da venda", "Preço", "Quantidade"), key="3")
    if colunas == "Clientes":
        colunas = "cliente"
    elif colunas == "Produto":
        colunas = "produto"
    elif colunas == "Data da venda":
        colunas = "data_venda"
    elif colunas == "Preço":
        colunas = "preco"
    elif colunas == "Quantidade":
        colunas = "quantidade"

    id = st.text_input('ID da venda:', key="4",value=x)
    
    inputs = []
    inputs.append(valor_antes)
    inputs.append(valor_depois)
    inputs.append(colunas)
    inputs.append(id)
    print(inputs)

    confirmar = st.button('Confirmar', on_click=clear_text)
    if confirmar:
        valor_antes = inputs[0]
        valor_depois = inputs[1]
        colunas = inputs[2]
        id = inputs[3]

        if colunas in col_int:
            valor_antes = float(valor_antes)
            valor_depois = float(valor_depois)
            comando = f'UPDATE vendas SET {colunas} = {valor_depois} WHERE id_venda = {id}'
        else:
            comando = f"UPDATE vendas SET {colunas} = '{valor_depois}' WHERE id_venda = {id}"

        cursor.execute(comando)
        conexao.commit()
        st.success('Alterações concluidas com sucesso!')
        clear_text()
        time.sleep(5)
        st.rerun()
def deletar_valores():
    st.subheader("Preencha os dados para fazer a alteração")
    st.write('Tabela Atual:')
    visualizar_tabela()
    
if choice == "Adicionar Valores":
    adicionar_valores()
        
elif choice == "Visualizar Tabela":
    visualizar_tabela()

elif choice == "Mudar Valores":
    mudar_valores()

else:
    deletar_valores()
