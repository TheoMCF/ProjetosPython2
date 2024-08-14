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
col1, col2, col3, col4 = st.columns(4, gap='small')
st.title('Manilpulação de Dados SQL')
tab1, tab2, tab3, tab4 = st.tabs(["Visualizar Tabela","Adicionar Valores" ,"Mudar Valores", "Deletar Linhas",])

def adicionar_valores():
    st.subheader("Adicionar novos dados:")
    visualizar_tabela()
    with st.form(key='AdicionarValores', clear_on_submit=True):
        cliente = st.text_input("Nome do cliente: ")
        produto = st.text_input("Produto: ")
        data_venda = str(st.date_input('Data da venda: '))      
        preco = st.text_input('Preço do produto: ')
        quantidade = st.number_input('Quantidade de produtos: ', 0)
        idvenda = st.number_input('ID da venda: ', 0)
        confirmar1 = st.form_submit_button('Confirmar')
        
        if confirmar1:
            preco = float(preco)
            comando = f"INSERT INTO vendas (cliente, produto, data_venda, preco, quantidade, id_venda) VALUES ('{cliente}', '{produto}', '{data_venda}', {preco}, {quantidade}, {idvenda})"
            cursor.execute(comando)
            conexao.commit()
            st.success('Conexão Concluida!')
            time.sleep(5)
            st.rerun()
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
            linha = {"ID da venda": f"{id[j]}", "Cliente": f"{clientes[j]}", "Produto": f"{produtos[j]}", "Data da venda": f"{datas[j]}", "Preço" : f"{precos[j]}", "Quantidade" : f"{quantidade[j]}"}
            df1 = df1._append(linha, ignore_index = True)
            j +=1
        st.subheader('Tabela Atual')
        st.dataframe(df1, hide_index=True)
def mudar_valores():
    col_int = ["preco", "quantidade"]
    st.subheader("Alterar a tabela:")
    visualizar_tabela()
    with st.form(key='MudarValores', clear_on_submit=True):
        valor_antes = st.text_input('Valor a ser alterado:')
        valor_depois = st.text_input("Esse valor será subistituido por:")

        colunas = st.selectbox("Coluna onde ele está:", ("","Clientes", "Produto", "Data da venda", "Preço", "Quantidade", "ID da venda"))
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
        else:
            colunas = "id_venda"
        id = st.number_input('ID da venda:', 0)
        
        inputs = []
        
        inputs.append(valor_antes)
        inputs.append(valor_depois)
        inputs.append(colunas)
        inputs.append(id)

        confirmar2 = st.form_submit_button('Confirmar')
        if confirmar2:
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
            time.sleep(5)
            st.rerun()
def deletar_valores():
    st.subheader("Deletar valores da tabela:")
    visualizar_tabela()
    with st.form(key='DeletarLinhas', clear_on_submit=True):
        id = st.number_input('ID da linha que você quer deletar: ', 0 )

        comando = f'DELETE FROM vendas WHERE id_venda = {id}'

        confirmar3 = st.form_submit_button('Confirmar')
    
        if confirmar3:
            cursor.execute(comando)
            conexao.commit()
            st.success('Alterações concluidas com sucesso!')
            time.sleep(5)
            st.rerun()

with tab1:
    visualizar_tabela()
with tab2:
    adicionar_valores()
with tab3:
    mudar_valores()
with tab4:
    deletar_valores()