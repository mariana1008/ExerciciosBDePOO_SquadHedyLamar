import datetime
import sqlite3

conexao = sqlite3.connect('banco_biblioteca.db')
cursor = conexao.cursor()

class Emprestimo:
    def __init__(self,id_titulo, data_emprestimo):
        self.id_emprestimo = id
        self.id_titulo = id_titulo
        self.data_emprestimo = datetime.datetime.now()
        self.data_devolucao = data_emprestimo + datetime.timedelta(days=15)
        self.estado_exemplar = ''
        #cursor.execute('INSERT INTO emprestimos (id_titulo, data_emprestimo, data_devolucao, estado_exemplar) VALUES (?, ?, ?, ?)',(self.id_titulo, self.data_emprestimo, self.data_devolucao, self.estado_exemplar))
        
    def realizar_emprestimo(self):
        #nao deixar realiar emprestimo sem livros no banco de dados
        cursor.execute('SELECT id_exemplar FROM exemplares WHERE id_livro = ? AND disponivel = ? LIMIT 1', (self.id_titulo, True))
        id_exemplar = cursor.fetchone()
        if id_exemplar:
            id_exemplar_estado = id_exemplar[0]
            cursor.execute('UPDATE exemplares SET disponivel = ? WHERE id_exemplar = ?', (False, id_exemplar_estado))
            print(f"Empréstimo realizado com sucesso para o exemplar {id_exemplar_estado}.")
            self.estado_exemplar = 'Emprestado'
            cursor.execute('INSERT INTO emprestimos (id, data_emprestimo, data_devolucao, estado_exemplar) VALUES (?, ?, ?, ?)',(id_exemplar_estado, self.data_emprestimo, self.data_devolucao, self.estado_exemplar))
            print(f"Data de devolução: {self.data_devolucao}")
        else:
            print("não existem mais exemplares disponiveis")
      
    def realizar_devolucao(self,id_exemplar_emprestado):
       cursor.execute('SELECT id_exemplar FROM exemplares WHERE id_exemplar = ? AND disponivel = ? LIMIT 1', (id_exemplar_emprestado, False))
       id_exemplar = cursor.fetchone()
       if id_exemplar:
            print(f"Devolução realizada para o livro exemplar {id_exemplar[0]}")
            cursor.execute('UPDATE exemplares SET disponivel = ? WHERE id_exemplar = ?', (True, id_exemplar_emprestado))
            self.estado_exemplar = 'Disponivel'
            cursor.execute('UPDATE emprestimos SET estado_exemplar = ? WHERE id =? ',(self.estado_exemplar,id_exemplar_emprestado))
       else:
           print(f"O exemplar {id_exemplar_emprestado} já foi devolvido")        

    def renovar_emprestimo(self, id_exemplar):
        cursor.execute('SELECT data_devolucao FROM emprestimos WHERE id = ?',(id_exemplar,))
        data_devolucao = cursor.fetchone()[0]
        data_devolucao_convertida = datetime.datetime.strptime(data_devolucao, '%Y-%m-%d %H:%M:%S.%f' )
        if data_devolucao:
            nova_data = data_devolucao_convertida + datetime.timedelta(days=15)
            cursor.execute('UPDATE emprestimos SET data_devolucao = ? WHERE id = ?',(nova_data,id_exemplar))
            print('emprestimo renovado com sucesso')
    
    

        

data_emprestimo = datetime.datetime.now()
emprestimo = Emprestimo(4,data_emprestimo=data_emprestimo)
#emprestimo.realizar_emprestimo()
#emprestimo.realizar_devolucao(7)
emprestimo.renovar_emprestimo(1)
conexao.commit()
conexao.close()