from classe_abstrata import Biblioteca
import datetime
import sqlite3

conexao = sqlite3.connect('banco_biblioteca.db')
cursor = conexao.cursor()

class Livro(Biblioteca):
    def __init__(self,id,titulo,editora,genero,exemplares):
        super().__init__()
        self._id_livro = id
        #self._autores = autor
        self._titulo = titulo
        self._editora = editora
        self._genero = genero
        self._total_exemplares = exemplares
        self.id = 0 
       
    def cadastrar_Livro(self):
        #não deixar cadastrar livro com mesmo nome
        livros = cursor.execute('SELECT titulo From livros') 
        lista_livros = []
        for livro in livros:
            lista_livros.append(livro[0])
        
        if self._titulo in lista_livros:
            print("livro já cadastrado")
        else:
            cursor.execute('INSERT INTO livros(id_titulo, titulo, editora, genero, numero_exemplar) VALUES (?, ?, ?, ?, ?)',(self._id_livro, self._titulo, self._editora, self._genero, self._total_exemplares))
            print(f"Livro {self._titulo} cadastrado com sucesso!")
            
            for i in range(self._total_exemplares):
                cursor.execute('INSERT INTO exemplares(id_livro, disponivel) VALUES (?, ?)', (self._id_livro, True))
            print(f"{self._total_exemplares} exemplares cadastrados para o livro {self._titulo}")
       
    def cadastrar_autor(self,id_autor,nome_autor):
        nomes_autores_lista = []
        nomes = cursor.execute("SELECT nome_autor FROM autores")
                
        for nome in nomes:
            nomes_autores_lista.append(nome[0])
        
        if nome_autor in nomes_autores_lista:
            print(" autor ja cadastrado")
        else:
            cursor.execute('INSERT INTO autores VALUES (?,?)',(id_autor,nome_autor))    
            print(nome_autor)
            
    def adicionar_autor_ao_livro(self,id_autor):
        ids_autores = []
        id_autor_verificado = []
        
        verifica_existe_autor = cursor.execute('SELECT id_autor FROM autores')
        for verificar in verifica_existe_autor:
            id_autor_verificado.append(verificar[0])
        
        adicionar_autor = cursor.execute('SELECT id_autor FROM livro_autores')
        for adicionar in adicionar_autor:
            ids_autores.append(adicionar[0])
       
        if id_autor in id_autor_verificado:
            if id_autor in ids_autores:
                print('Autor já foi adicionado ao livro')
            else:
                cursor.execute("INSERT INTO livro_autores VALUES (?,?)",(self._id_livro,id_autor))
        else:
            print('não existe um autor com esse id')
    
    def imprimir(self):
        print(f"Titulo: {self._titulo} \nAutores: {self._autores} \nExemplares: {self._lista_exemplares}")

ceu_esta_em_todo_lugar = Livro(4,'monitor', 'Editora A', 'Ficção Científica', 10)
ceu_esta_em_todo_lugar.cadastrar_Livro()

#ceu_esta_em_todo_lugar.realizar_emprestimo()

#ceu_esta_em_todo_lugar.realizar_devolucao(1)

#ceu_esta_em_todo_lugar.cadastrar_autor(20,"pedro")
#ceu_esta_em_todo_lugar.adicionar_autor_ao_livro(20)


conexao.commit()
conexao.close()