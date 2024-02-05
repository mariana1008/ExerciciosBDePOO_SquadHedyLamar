from abc import ABC, abstractmethod

class AbstrataBiblioteca(ABC):
    def __init__(self,nome,telefone,nacionalidade,livro):
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade
        self._nome_livro = livro
    @abstractmethod
    def usuario(self):
        pass    
    
    @abstractmethod
    def cadastrar_Livro(self):
        pass
    
    @abstractmethod
    def realizar_emprestimo(self):
        pass
    
    @abstractmethod
    def realizar_devolucao(self):
        pass
    
class Biblioteca(AbstrataBiblioteca):
    def __init__(self,nome,telefone,nacionalidade,livro):
        super().__init__(nome,telefone,nacionalidade,livro)
     
    def usuario(self):
        print(f"Usuário {self.nome} cadastrado com sucesso!")    
    
    def cadastrar_Livro(self):
        print(f"Livro tal cadastrado com sucesso!")
    
    def realizar_emprestimo(self):
        print(f"Empréstimo realizado para nome.usuario: nome.livro")
    
    def realizar_devolucao(self):
        print(f"Devolução realizada por nome.usuario: nome.livro")
