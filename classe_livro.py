from classe_abstrata_ import Biblioteca
import sqlite3

# Inicia conexão com o Banco de Dados
conexao = sqlite3.connect('banco_biblioteca.db')
cursor = conexao.cursor()

# Inicia classe Livro que herda de Bilioteca
class Livro(Biblioteca):
    def __init__(self, id, titulo, editora, genero, exemplares):
        super().__init__()
        self._id = id
        self._titulo = titulo
        self._editora = editora
        self._genero = genero
        self._total_exemplares = exemplares
        self.autores = [] 
        self.id_exemplares = {i: True for i in range(1, exemplares + 1)} # Controle dos exemplares disponíveis com dicionário

    # Cadastra um livro no sistema e adiciona informações ao banco de dados
    def cadastrar_livro(self):
        for autor in self.autores:
            cursor.execute('INSERT INTO autores (nome_autor) VALUES (?)', (autor,))
            conexao.commit()

        cursor.execute('INSERT INTO livros (titulo, editora, genero, numero_exemplar) VALUES (?, ?, ?, ?)', (self._titulo, self._editora, self._genero, self._total_exemplares))
        conexao.commit()

        i = 1
        while i <= self._total_exemplares:
            self.id_exemplares[i] = True
            i += 1

        print(f"Livro {self._titulo} cadastrado com sucesso!\n")

    # Adiciona autores ao livro e adiciona informações ao banco de dados
    def adicionar_autor(self, autores):
        if isinstance(autores, str):
            autores = [autores]
            
            for autor in autores:
                cursor.execute('INSERT INTO autores (nome_autor) VALUES (?)', (autor,))
                conexao.commit()

        self.autores.extend(autores)

        # Formatação da saída de informações
        autores_formatados = ', '.join(self.autores)
        print(f'Autor(es) {autores_formatados} inserido(os) com sucesso!\n')
        
    # Verifica se há exemplares disponíveis e atualiza informações ao banco de dados
    def realizar_emprestimo(self):
        if self._total_exemplares > 0:
            self.id, boleano = self.id_exemplares.popitem()
            self._total_exemplares -= 1
            print(f"Empréstimo realizado para o livro {self._titulo}, Exemplar {self.id}.\n")

            cursor.execute('UPDATE livros SET numero_exemplar = numero_exemplar - 1 WHERE id = ? ', (self.id,))
            conexao.commit()

        else:
            print("Não existem mais exemplares disponíveis!\n")

    # Parte do método imprimir, mostra informações formatadas sobre o livro
    def imprimir(self):
        print(f"Título: {self._titulo} \nAutor(es): {', '.join(self.autores)} \nExemplares: {self._total_exemplares}\n")

    # Método especial __str__ que retorna uma representação formatada em string do objeto 
    def __str__(self):
        return f"Informações do livro \nID: {self._id}, \nTítulo: {self._titulo}, \nEditora: {self._editora}, \nGênero: {self._genero}, \nExemplares: {self._total_exemplares}, \nAutor(es):{self.autores}\n"

############################## TESTES
    
# Adicionar autores e imprimir informações
livro1 = Livro(id=1, titulo="Livro A", editora="Editora1", genero="Gênero1", exemplares=5)
print(livro1)
livro1.adicionar_autor("Autor1")
print(livro1)
livro1.adicionar_autor("Autor2")
print(livro1)
livro1.cadastrar_livro()
print(livro1)

# Realizar um empréstimo e imprimir informações
livro1.realizar_emprestimo()
print(livro1)

# Imprimir informações após o empréstimo
livro1.imprimir()

# Adicionar autores e imprimir informações
livro1.adicionar_autor(["Autor3", "Autor4", "Autor5"])
print(livro1)

# Tentar emprestar mais exemplares do que tem e imprimir informações
for _ in range(6):
    livro1.realizar_emprestimo()
print(livro1)

# Imprimir informações após os empréstimos
livro1.imprimir()

# Criar livro_teste, adicionar autores e imprimir informações
livro_teste = Livro(id=1, titulo="Livro Teste", editora="Editora Teste", genero="Gênero Teste", exemplares=3)
livro_teste.adicionar_autor("Autor Teste1")
livro_teste.adicionar_autor(["Autor Teste2", "Autor Teste3"])
livro_teste.imprimir()

# Finaliza conexão com o Banco de Dados
conexao.close()