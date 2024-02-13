import datetime
import sqlite3

conexao = sqlite3.connect('banco_biblioteca.db')
cursor = conexao.cursor()

class Emprestimo:
    def __init__(self, id_titulo, data_emprestimo):
        self.id_emprestimo = id
        self.id_titulo = id_titulo
        self.data_emprestimo = datetime.datetime.now()
        self.data_devolucao = data_emprestimo + datetime.timedelta(days=15)
        self.estado_exemplar = 'Emprestado'

        cursor.execute('INSERT INTO emprestimos (id_titulo, data_emprestimo, data_devolucao, estado_exemplar) VALUES (?, ?, ?, ?)',(self.id_titulo, self.data_emprestimo, self.data_devolucao, self.estado_exemplar))
        
        conexao.commit()
        conexao.close()

    def imprimir_info(self):
        print(f"Emprestado livro com ID {self.id_titulo} em {self.data_emprestimo}")
        print(f"Data de devolução: {self.data_devolucao}")

data_emprestimo = datetime.datetime.now()
emprestimo = Emprestimo(id_titulo=4, data_emprestimo=data_emprestimo)
emprestimo.imprimir_info()