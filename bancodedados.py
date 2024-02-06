import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('banco_biblioteca.db')
print("Conexão bem-sucedida!")

# Passando a conexão para uma nova variável
cursor = conexao.cursor()

"""1. Criação de tabelas"""    
cursor.execute('CREATE TABLE livros(id INT, autor VARCHAR(100), titulo VARCHAR(100), editora VARCHAR(100), genero VARCHAR(50), numero_exemplar INT)')
cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), telefone VARCHAR(15), nacionalidade VARCHAR(100))')
# Data fica como AAAA-MM-DD
cursor.execute('CREATE TABLE emprestimos(id INT, data_emprestimo DATE,  data_devolucao DATE, estado_exemplar VARCHAR(100))')

"""2. Inserção de Dados"""    

"""3. Consultas SQL"""    

"""4. Atualizações e exclusões"""    

# Envio das informações para o banco
conexao.commit()
print("Comando executado com sucesso!")

conexao.close()