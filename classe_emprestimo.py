from classe_abstrata import Biblioteca

class Emprestimo(Biblioteca):
    def __init__(self,nome,livro,data,devolucao,estado_livro):
        super().__init__(nome,livro)
        self._data_emprestimo = data
        self._data_devolucao = devolucao
        self._estado_exemplar = estado_livro
        self._titulo = livro
        
    def realizar_emprestimo(self):
        print(f"Empréstimo realizado para {self.nome}: {self._titulo}")
        return super().realizar_emprestimo()
    
    