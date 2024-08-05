import pyodbc as py
import streamlit as st
from datetime import datetime as dt
dados_conexao = (
    "Driver={SQL Server};"
    "Server=wiliam;"
    "Database=PythonSQL;"
)

conexao = py.connect(dados_conexao)
cursor = conexao.cursor()

operação = int(input('Digite 1 para CREATE, 2 para READ, 3 para UPDATE e 4 para DELETE: '))

if operação == 1:
    id_venda = int(input('ID da venda: '))
    cliente = input('Cliente: ')
    produto = input('Produto: ')
    data_venda = input('Data da venda: ')
    preco = float(input('Preço do produto: '))
    quantidade = int(input('Quantidade de produtos: '))

    comando = f"INSERT INTO vendas (id_venda, cliente, produto, data_venda, preco, quantidade) VALUES ({id_venda}, '{cliente}', '{produto}', '{data_venda}', {preco}, {quantidade})"
    cursor.execute(comando)
    conexao.commit()

if operação == 2:
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(resultado)
if operação == 3:
    comando = "UPDATE vendas SET id_venda = 3 WHERE cliente = 'Alice'"
    cursor.execute(comando)
    conexao.commit()
if operação == 4:
    comando = f"DELETE FROM vendas WHERE cliente = 'Lira'"
    cursor.execute(comando)
    conexao.commit()
else:
    print('Operação inválida')

cursor.close() 
conexao.close()
print(' \n Conexão bem sucedida')