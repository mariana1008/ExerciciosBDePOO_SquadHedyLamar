from classe_abstrata import Biblioteca
import sqlite3

conexao = sqlite3.connect('banco_biblioteca.db')
cursor = conexao.cursor()

class Livro(Biblioteca):
    def __init__(self,id,autor,titulo,editora,genero,exemplares):
        super().__init__()
        self._id = id
        self._autores = autor
        self._titulo = titulo
        self._editora = editora
        self._genero = genero
        self._total_exemplares = exemplares
        self.id = 0 
       
    def cadastrar_Livro(self):
        cursor.execute('INSERT INTO livros(id, autor, titulo, editora, genero, numero_exemplar) VALUES (?, ?, ?, ?, ?, ?)',(self._id, self._autores, self._titulo, self._editora, self._genero, self._total_exemplares))
        print(f"Livro {self._titulo} cadastrado com sucesso!")
    
    def adicionar_autor(self,autor):
       #cursor.execute('INSERT INTO livros(id,autor) ')
        self._autores.append(autor)
    
    def realizar_emprestimo(self):
        if self._total_exemplares > 0:
            print(f"Empréstimo realizado para o livro {self._titulo}")
            self._total_exemplares -= 1
            cursor.execute('UPDATE livros SET numero_exemplar = ? WHERE id = ?', (self._total_exemplares, self._id))
        else:
            print("não existem mais exemplares disponiveis")
            
    
    def imprimir(self):
        print(f"Titulo: {self._titulo} \nAutores: {self._autores} \nExemplares: {self._lista_exemplares}")

ceu_esta_em_todo_lugar = Livro(1,"Jandy","Céu está em todo lugar", "Campus","Romance",3)
#ceu_esta_em_todo_lugar.cadastrar_Livro()
ceu_esta_em_todo_lugar.realizar_emprestimo()
ceu_esta_em_todo_lugar.realizar_emprestimo()
ceu_esta_em_todo_lugar.realizar_emprestimo()
ceu_esta_em_todo_lugar.realizar_emprestimo()


conexao.commit()
conexao.close()