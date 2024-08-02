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

# Create
nome_produto = 'Mangá'
valor = 42
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", "{valor}")' #insere uma informação
cursor.execute(comando) #executa o comando
conexao.commit() #manda pra o banco de dados

# Read
comando = 'SELECT * FROM vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

# Update
comando = 'UPDATE vendas SET valor = 2000 WHERE nome_produto = "Rolex"'
cursor.execute(comando)
conexao.commit()

# Delete
comando = 'DELETE FROM vendas WHERE idvendas = 3'
cursor.execute(comando)
conexao.commit()


cursor.close() 
conexao.close() # fecha a conexão com o banco de dados