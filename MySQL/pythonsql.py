import pyodbc as py
dados_conexao = (
    "Driver={SQL Server};"
    "Server=wiliam;"
    "Database=PythonSQL;"
)
conexao = py.connect(dados_conexao)
cursor = conexao.cursor()
colunas_str = ['cliente','produto',	'data_venda']
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

elif operação == 2:
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    print(f'A tabela está assim: \n {resultado}')

elif operação == 3:
    w = input('Defina o novo valor de W:\nUPDATE vendas W = X WHERE Y = Z: ')
    x = input(f'Defina o valor de X:\nUPDATE vendas {w} = X WHERE Y = Z: ')
    y = input(f'Defina o valor de Y:\nUPDATE vendas {w} = {x} WHERE Y = Z: ')
    z = input(f'Defina o valor de Z:\nUPDATE vendas {w} = {x} WHERE {y} = Z: ')
    if y in colunas_str:
        comando = f"UPDATE vendas SET {w} = {x} WHERE {y} = '{z}'"
    else:
        comando = f"UPDATE vendas SET {w} = {x} WHERE {y} = {z}"
    cursor.execute(comando)
    conexao.commit()

elif operação == 4:
    a = input('Defina o valor de A:\nDELETE FROM vendas WHERE A = B: ')
    b = input('Defina o valor de B:\nDELETE FROM vendas WHERE A = B: ')
    if a in colunas_str:
        comando = f"DELETE FROM vendas WHERE {a} = '{b}'"
    else:
        comando = f"DELETE FROM vendas WHERE {a} = {b}"
    cursor.execute(comando)
    conexao.commit()

else:
    print('Operação inválida')

cursor.close() 
conexao.close()
print(' \n Conexão bem sucedida')