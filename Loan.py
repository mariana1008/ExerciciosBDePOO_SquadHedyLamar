from time import datetime

class Loan:
    def __init__(self, usuario, exemplar):
        self.usuario = usuario
        self.exemplar = exemplar
        self.data_emprestimo = datetime.now()
        self.renovacoes = 0

    def renovar(self):
        if self.renovacoes < 3:
            self.data_emprestimo = datetime.now()
            self.renovacoes += 1
        else:
            raise ValueError("Número máximo de renovações atingido")
    
    def devolver(self):
        self.exemplar.disponiveis.append(self.exemplar)
        self.data_devolucao = datetime.now()
        self.exemplar = None

    def __str__(self):
        return f"{self.exemplar.livro.titulo}, {self.usuario.nome}"