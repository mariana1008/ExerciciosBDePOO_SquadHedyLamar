from abc import  ABC, abstractmethod
import sqlite3




class conexaoBD:
    def __init__(self, banco_biblioteca):
        # Iniciando a conexão e o cursor
        self.conexao = sqlite3.connect(banco_biblioteca)
        self.cursor = self.conexao.cursor()
    
    

class AbstrataBiblioteca(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def usuario(self):
        pass    
        
    @abstractmethod
    def realizar_emprestimo(self):
        pass
    
    @abstractmethod
    def realizar_devolucao(self):
        pass

class Biblioteca(AbstrataBiblioteca):
    def __init__(self):
        super().__init__()
     
    def usuario(self):
        print(f"Usuário cadastrado com sucesso!")    
                    
    def realizar_emprestimo(self):
        print(f"Empréstimo realizado ")
    
    def realizar_devolucao(self):
        print(f"Devolução realizada ")
        