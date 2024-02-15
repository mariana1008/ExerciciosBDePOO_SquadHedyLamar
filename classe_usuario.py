import sqlite3

conexao = sqlite3.connect('banco_biblioteca.db')
cursor = conexao.cursor()

class Usuario:
    def __init__(self, nome, telefone, nacionalidade, cargo):
        self.id = None
        self.nome =  nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade
        self.cargo = cargo
        
    
    def inserirUsuario(self, nome, telefone, nacionalidade, cargo):
        # Verificar se o cargo é 'Administrador' antes de permitir a inserção
        if self.cargo == 'Administrador':
            cursor.execute('INSERT INTO usuarios(nome, telefone, nacionalidade, cargo) VALUES(?,?,?,?)', (nome, telefone, nacionalidade, cargo))
            conexao.commit()
            print("Usuário inserido com sucesso!")
        else:
            print("Permissão negada. Apenas administradores podem inserir usuários.")
        
    def removerUsuarioPorId(id):
        cursor.execute('DELETE FROM usuarios where id=?',(id,))
        conexao.commit()

    def listarUsuarios(self):
        dados = cursor.execute('SELECT * FROM usuarios ORDER BY nome')
        for usuario in dados:
            print(usuario)
        conexao.commit()
    def removerUsuarios():
        cursor.execute('DELETE FROM usuarios')
        conexao.commit()
    
    def atualizarUsuario(self, nome, novo_telefone, nova_nacionalidade):
        if self.cargo == 'Administrador':
            cursor.execute('UPDATE usuarios SET telefone=?, nacionalidade=? WHERE nome=?',
                           (novo_telefone, nova_nacionalidade, nome))
            conexao.commit()
            print("Usuário atualizado com sucesso!")
        else:
            print("Permissão negada. Apenas administradores podem atualizar usuários.")
    
    def obterUsuarioPorNome(self, nome):
        # Retorna informações do usuário com base no nome
        dados = cursor.execute('SELECT * FROM usuarios WHERE nome=?', (nome,))
        return dados.fetchone()        