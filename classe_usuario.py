import sqlite3
from classe_abstrata import conexaoBD

conexao = conexaoBD('banco_biblioteca')
cursor = conexao.cursor

class Usuario:
    def __init__(self, id, nome, telefone, nacionalidade):
        self.id =  id
        self.nome =  nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

        
    def inserirUsuario(self):
        cursor.execute('INSERT INTO usuarios(id, nome, telefone, nacionalidade) VALUES(?,?,?,?)',(self.id, self.nome, self.telefone, self.nacionalidade))
        conexao.commit()
        
    def removerUsuarioPorId(id):
        cursor.execute('DELETE FROM usuarios where id=?',(id,))
        conexao.commit()

    def listarUsuarios():
        dados = cursor.execute('SELECT * FROM usuarios ORDER BY nome')
        for usuario in dados:
            print(usuario)
        conexao.commit()

    def removerUsuarios():
        cursor.execute('DELETE FROM usuarios')
        conexao.commit()
        
    def atualizarUsuario(self):
        self.id =  ''
        #cursor.execute('UPDATE')

conexao.fechar_conexao()