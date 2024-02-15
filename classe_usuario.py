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
        
    def removerUsuarioPorId(self, id):
    # Verificar se o cargo é 'Administrador' antes de permitir a remoção
        if self.cargo == 'Administrador':
            cursor.execute('DELETE FROM usuarios WHERE id=?', (id,))
            conexao.commit()
            print(f"Usuário com ID {id} removido com sucesso!")
        else:
            print("Permissão negada. Apenas administradores podem remover usuários.")
            
    def listarUsuarios(self):
        if self.cargo in ['Administrador', 'Master']:
            dados = cursor.execute('SELECT * FROM usuarios ORDER BY nome')
            for usuario in dados:
                print(usuario)
            conexao.commit()
        else:
            print("Permissão negada. Apenas administradores e masters podem listar usuários.")
        
    def removerUsuarios(self):
        # Verificar se o cargo é 'Master' antes de permitir a remoção de todos os usuários
        if self.cargo == 'Master':
            cursor.execute('DELETE FROM usuarios')
            conexao.commit()
            print("Todos os usuários removidos com sucesso!")
        else:
            print("Permissão negada. Apenas usuários com cargo 'Master' podem remover todos os usuários.")
    
    def atualizarUsuario(self, nome, novo_telefone, nova_nacionalidade):
        if self.cargo in ['Administrador','Master']:
            cursor.execute('UPDATE usuarios SET telefone=?, nacionalidade=? WHERE nome=?',
                           (novo_telefone, nova_nacionalidade, nome))
            conexao.commit()
            print("Usuário atualizado com sucesso!")
        else:
            print("Permissão negada. Apenas administradores podem atualizar usuários.")
    
    def obterUsuarioPorNome(self, nome):
        # Verificar se o cargo é 'Administrador' ou 'Master' antes de permitir a consulta
        if self.cargo in ['Administrador', 'Master']:
            dados = cursor.execute('SELECT * FROM usuarios WHERE nome=?', (nome,))
            return dados.fetchone()
        else:
            print("Permissão negada. Apenas administradores e masters podem consultar usuários.")
            return None      