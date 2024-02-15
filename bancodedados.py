import sqlite3

# Conexão com o banco de dados
conexao = sqlite3.connect('banco_biblioteca.db')
print("Conexão bem-sucedida!")

# Passando a conexão para uma nova variável
cursor = conexao.cursor()

#1. Criação de tabelas
            #-------------------------#----------#
"""Recriando tabelas necessarias para a parte de emprestimo, relação de muito para muitos
    cursor.execute('CREATE TABLE autores(id_autor INTEGER PRIMARY KEY AUTOINCREMENT, nome_autor VARCHAR(100))')
    cursor.execute('CREATE TABLE livros(id_livro INTEGER PRIMARY KEY AUTOINCREMENT, titulo VARCHAR(100), editora VARCHAR(100), genero VARCHAR(50), numero_exemplar INT)')
    cursor.execute('CREATE TABLE livro_autores(id_livro INTEGER, id_autor INTEGER, FOREIGN KEY (id_livro) REFERENCES livros(id_livro), FOREIGN KEY (id_autor) REFERENCES autores(id_autor))')
    cursor.execute('CREATE TABLE exemplares(id_exemplar INTEGER PRIMARY KEY AUTOINCREMENT, id_livro INTEGER, disponivel BOOLEAN, FOREIGN KEY (id_livro) REFERENCES livros(id_livro))')
"""

"""Criação feita anteriormente, temos tbm mudanças da tabela usuario inclusas aqui.
#cursor.execute('CREATE TABLE livros(id INT, autor VARCHAR(100), titulo VARCHAR(100), editora VARCHAR(100), genero VARCHAR(50), numero_exemplar INT)')
#cursor.execute('CREATE TABLE autores(id_autor INTEGER PRIMARY KEY, nome_autor VARCHAR(100))')
#cursor.execute('CREATE TABLE livro_autores(id_livro INTEGER, id_autor INTEGER, FOREIGN KEY (id_livro) REFERENCES livros(id_titulo), FOREIGN KEY (id_autor) REFERENCES autores(id_autor))')
#cursor.execute('CREATE TABLE livros(id_titulo INTEGER PRIMARY KEY, titulo VARCHAR(100), editora VARCHAR(100), genero VARCHAR(50), disponiveis INT)')
#cursor.execute('''CREATE TABLE exemplares (id_exemplar INTEGER PRIMARY KEY AUTOINCREMENT,id_livro INTEGER,disponivel BOOLEAN,FOREIGN KEY (id_livro) REFERENCES livros(id_livro))''')
#cursor.execute('CREATE TABLE usuarios(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), telefone VARCHAR(15), nacionalidade VARCHAR(100), cargo VARCHAR(100))')
# Data fica como AAAA-MM-DD
#cursor.execute('CREATE TABLE emprestimos(id INT, data_emprestimo DATE,  data_devolucao DATE, estado_exemplar VARCHAR(100))')
""" 


#2. Inserção de Dados   
# Inserindo dados em usuarios
#lista_nomes = ['Amanda', 'Gabriella', 'Jéssica', 'Hevilin', 'Fernanda', 'Lais', 'Raquel', 'Jhenyffer', 'Sara',  'Martha', 'Mariana'] 
# 
#for nome in lista_nomes:linha alterada pois a tabela passou a ser autoincremento logo sem necessidade de colocarmos o id manualmente.
 #   cursor.execute('INSERT INTO usuarios(nome, telefone, nacionalidade, cargo) VALUES(?,?,?,?)',(nome, '3433333333', 'BR', 'comum'))

"""Parte em que iremos colocar livros e altores
lista_livros = [
    ('Harry Potter', 'Editora1', 'Fantasia', 5),
    ('1984', 'Editora2', 'Ficção Científica', 7),
    ('Dom Quixote', 'Editora3', 'Romance', 10),
    ('A Revolta de Atlas', 'Editora4', 'Filosofia', 3),
    ('Cem Anos de Solidão', 'Editora5', 'Realismo Mágico', 8),
    ('O Senhor dos Anéis', 'Editora6', 'Fantasia', 6),
    ('Crime e Castigo', 'Editora7', 'Romance Psicológico', 4),
    ('Orgulho e Preconceito', 'Editora8', 'Romance Clássico', 9),
    ('O Pequeno Príncipe', 'Editora9', 'Fábula', 12),
    ('Duna', 'Editora10', 'Ficção Científica', 6),
    ('Revolução dos Bichos', 'Editora11', 'Alegoria', 5), 
]
#inserir livros no nosso banco 
cursor.executemany('INSERT INTO livros(titulo, editora, genero, numero_exemplar) VALUES (?, ?, ?, ?)', lista_livros)
"""

"""Inserindo lista de autores para podermos relacionar com livros
lista_autores = [
    ('JK Rowling',),
    ('George Orwell',),
    ('Miguel de Cervantes',),
    ('Ayn Rand',),
    ('Gabriel Garcia Márquez',),
    ('J.R.R. Tolkien',),
    ('Fiódor Dostoiévski',),
    ('Jane Austen',),
    ('Antoine de Saint-Exupéry',),
    ('Frank Herbert',),
]

cursor.executemany('INSERT INTO autores(nome_autor) VALUES (?)', lista_autores)
"""
"""Começando aqui a parte de relação de autor e livro
ids_autores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ids_livros = list(range(1, 12))  # IDs dos livros de 1 a 11

# Relacionando autores aos livros
dados_livro_autores = [(id_livro, id_autor) for id_livro in ids_livros for id_autor in ids_autores]

# Inserindo dados na tabela livro_autores
cursor.executemany('INSERT INTO livro_autores(id_livro, id_autor) VALUES (?, ?)', dados_livro_autores)
"""


"""
cursor.execute('''
    SELECT livro_autores.id_livro, livros.titulo, livro_autores.id_autor, autores.nome_autor
    FROM livro_autores
  INNER JOIN livros ON livro_autores.id_livro = livros.id_livro
    INNER JOIN autores ON livro_autores.id_autor = autores.id_autor
''')

 #Recuperando todos os resultados
dados_livro_autores_com_nomes = cursor.fetchall()
#Exibindo os resultados
for dado in dados_livro_autores_com_nomes:
 print(dado)
"""

 

"""Faltou resolver a questão de relacionar a tabela exemplar com sua coluna disponivel, 
a tabela livro e sua coluna de exemplares total"""

conexao.commit()

print("Atualização bem-sucedida!")

conexao.close()