from classe_abstrata import Biblioteca

class Emprestimo(Biblioteca):
    def __init__(self,nome,telefone,livro,data,devolucao,estado_livro):
        super().__init__(nome,telefone,livro)
        self._data_emprestimo = data
        self._data_devolucao = devolucao
        self._estado_exemplar = estado_livro
        
    def realizar_emprestimo(self):
        self._lista_exemplares -= 1
        print(f"Empréstimo realizado para {self.nome}: {self._nome_livro}")
        return super().realizar_emprestimo()
    
    