import mysql.connector
# CRUD = Create
#        Read
#        Update
#        Delete
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Friguifri",
    database="mysql (teste)"
)
cursor = conexao.cursor()

#Create
nome_produto = 'Mangá'
valor = 47.99
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", "{valor}")' #insere uma informação
cursor.execute(comando)
conexao.commit() #edita o banco de dados

cursor.close()
conexao.close()