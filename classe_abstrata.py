from abc import  ABC, abstractmethod


class AbstrataBiblioteca(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def cadastrar_livro(self):
        pass
    
    @abstractmethod
    def adicionar_autor(self, autores):
        pass
    
    @abstractmethod
    def realizar_emprestimo(self):
        pass
    
    @abstractmethod
    def imprimir(self):
        pass

class UsuarioAbstrato(ABC):
    def __init__(self, nome, telefone, nacionalidade):
        self._id = None
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, novo_id):
        if self._id is None:
            self._id = novo_id
        else:
            print("Não é possível alterar o ID após ser definido.")

class Biblioteca(AbstrataBiblioteca):
    def __init__(self):
        super().__init__()
     
    def cadastrar_livro(self):
        print(f"Livro cadastrado com sucesso!")    
                    
    def adicionar_autor(self, autores):
        print(f"Autores adicionados: {autores}")
    
    def realizar_emprestimo(self):
        print(f"Empréstimo realizado ")
    
    def imprimir(self):
        print(f"Imprimir informações do livro ")

class Usuario(UsuarioAbstrato):
    def __init__(self, nome, telefone, nacionalidade):
        super().__init__(nome, telefone, nacionalidade)

    def cadastrar_usuario(self):
        print(f"Usuário cadastrado com sucesso!") 

    def imprimir(self):
        print(f"Imprimir informações do usuário ")