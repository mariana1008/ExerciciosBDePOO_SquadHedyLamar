from classe_abstrata import Biblioteca

class Livro(Biblioteca):
    def __init__(self,titulo,exemplares,autores):
        super().__init__()
        self.id_exemplares = {}
        self._total_exemplares = exemplares
        self._lista_exemplares = exemplares 
        self._titulo = titulo
        self._autores = autores     
        self.id = 0   
        
    def cadastrar_Livro(self):
        i = 1
        while i <= self._total_exemplares:
            self.id_exemplares[i] = True
            i+=1
        #print(f"aqui tem id {self.id_exemplares}")
        print(f"Livro {self._titulo} cadastrado com sucesso!")
    
    def adicionar_autor(self,autor):
        self._autores.append(autor)
    
    def realizar_emprestimo(self):
        if self._lista_exemplares > 0:
            self.id, boleano = self.id_exemplares.popitem()
            #print(f"aqui tem id {self.id_exemplares}")  
            print(f"Empréstimo realizado para o livro {self._titulo}, Exemplar {self.id}.")
            self._lista_exemplares -= 1
        else:
            print("não existem mais exemplares disponiveis")
            
    
    def imprimir(self):
        print(f"Titulo: {self._titulo} \nAutores: {self._autores} \nExemplares: {self._lista_exemplares}")
        