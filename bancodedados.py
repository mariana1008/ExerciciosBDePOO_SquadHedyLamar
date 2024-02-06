import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('banco_biblioteca.db')
print("Conexão bem-sucedida!")
cursor = conexao.cursor()

#1. Criação de tabelas
# Criação das tabelas autores, livros, usuários e empréstimos
cursor.execute('CREATE TABLE autores(id_autor INTEGER PRIMARY KEY, nome_autor VARCHAR(100))')
cursor.execute('CREATE TABLE livros(id_titulo INT, id_autor INTEGER, titulo VARCHAR(100), editora VARCHAR(100), genero VARCHAR(50), numero_exemplar INT, FOREIGN KEY (id_autor) REFERENCES autores (id_autor))')
cursor.execute('CREATE TABLE usuarios(id_usuario INTEGER PRIMARY KEY, nome VARCHAR(100), telefone VARCHAR(15), nacionalidade VARCHAR(50))')
# Data fica como AAAA-MM-DD
cursor.execute('CREATE TABLE emprestimos(id_emprestimo INTEGER PRIMARY KEY, data_emprestimo DATE, data_devolucao DATE, estado_exemplar VARCHAR(100), id_usuario INTEGER, FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario))')


#2. Inserção de Dados
# Inserção de dados iniciais
cursor.execute("INSERT INTO autores VALUES (1, 'George Orwell')")
cursor.execute("INSERT INTO livros VALUES (1, 1, '1984', 'Editora A', 'Ficção Científica', 10)")
cursor.execute("INSERT INTO usuarios VALUES (1, 'Amanda', '123456789', 'Brasileira')")
cursor.execute("INSERT INTO emprestimos VALUES (1, '2023-01-15', '2023-02-15', 'Bom estado', 1)") 

# Inserindo dados em usuarios
lista_nomes = ['Amanda', 'Gabriella', 'Jéssica', 'Hevilin', 'Fernanda', 'Lais', 'Raquel', 'Jhenyffer', 'Sara',  'Martha', 'Mariana'] 

for index, nome in enumerate(lista_nomes):
    cursor.execute('INSERT INTO usuarios(id, nome, telefone, nacionalidade) VALUES(?,?,?,?)',(index, nome, '3433333333', 'BR'))
# Inserir mais conjuntos de dados


#3. Consultas SQL
"""
PESSOA 1:
- Listar todos os livros disponíveis.
- Encontrar todos os livros emprestados no momento.

PESSOA 2:
- Localizar os livros escritos por um autor específico.

PESSOA 3:
- Verificar o número de cópias disponíveis de um determinado livro.

PESSOA 4:
- Mostrar os empréstimos em atraso.
"""

#4. Atualizações e exclusões
"""
- Escreva consultas SQL para atualizar e excluir registros do banco de
dados, por exemplo, para marcar um livro como devolvido ou remover
um autor.
>>>>>>> Jhenyffer

PESSOA 1:
- Atualizar registros (inserção e atualização de dados em todas as tabelas)

PESSOA 2:
- Atualizar registros (exclusão de dados em todas as tabelas)
"""

# Envio das informações para o banco
conexao.commit()
print("Comando executado com sucesso!")

# Finaliza conexão com o Banco de Dados
conexao.close()