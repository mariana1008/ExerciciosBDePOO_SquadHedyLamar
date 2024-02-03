from abc import ABC, abstractmethod

class abstrataBiblioteca(ABC):
    def __init__(self,nome,telefone,nacionalidade):
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade
    
    @abstractmethod
    def usuario(self):
        pass    
    
    @abstractmethod
    def cadastroLivro(self):
        pass
    
    @abstractmethod
    def emprestimo(self):
        pass

