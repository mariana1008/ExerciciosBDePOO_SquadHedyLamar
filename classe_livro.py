from classe_abstrata import Biblioteca
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
        cursor.execute('INSERT INTO livros(id_titulo, titulo, editora, genero, numero_exemplar) VALUES (?, ?, ?, ?, ?)',(self._id_livro, self._titulo, self._editora, self._genero, self._total_exemplares))
        print(f"Livro {self._titulo} cadastrado com sucesso!")
    
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
       
       
    def realizar_emprestimo(self):
        if self._total_exemplares > 0:
            print(f"Empréstimo realizado para o livro {self._titulo}")
            self._total_exemplares -= 1
            cursor.execute('UPDATE livros SET numero_exemplar = ? WHERE id_titulo = ?', (self._total_exemplares, self._id_livro))
        else:
            print("não existem mais exemplares disponiveis")
      
    def realizar_devolucao(self):
        pass        

    def renovar_emprestimo(self):
        pass
    
    def imprimir(self):
        print(f"Titulo: {self._titulo} \nAutores: {self._autores} \nExemplares: {self._lista_exemplares}")

ceu_esta_em_todo_lugar = Livro(1,'1984', 'Editora A', 'Ficção Científica', 10)
#ceu_esta_em_todo_lugar.cadastrar_Livro()

for _ in range(11):
    ceu_esta_em_todo_lugar.realizar_emprestimo()

#ceu_esta_em_todo_lugar.cadastrar_autor(20,"pedro")
ceu_esta_em_todo_lugar.adicionar_autor_ao_livro(2220)


conexao.commit()
conexao.close()-